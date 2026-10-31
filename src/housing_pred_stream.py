# ================ #
# CARGAR LIBRERÍAS #
# ================ #
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ====================== #
# CONFIGURACIÓN DE RUTAS #
# ====================== #
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "model_linear_regression.joblib"
FEATURES_PATH = BASE_DIR / "models" / "features_linear_regression.joblib"

# ============= #
# CARGAR MODELO #
# ============= #
model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)

# ========================= #
# EXTRAER INFO DEL PIPELINE #
# ========================= #
preprocessor = model.named_steps['preprocessing']

cat_cols = preprocessor.transformers_[0][2]
num_cols = preprocessor.transformers_[1][2]

encoder = preprocessor.named_transformers_['cat']
categorias = encoder.categories_

cat_values = {
    col: list(vals)
    for col, vals in zip(cat_cols, categorias)
}

# ============================== #
# CONFIGURACIÓN DE LA APLICACIÓN #
# ============================== #
st.set_page_config(
    page_title="Predicción de Viviendas",
    layout="wide"
)

# ======================= #
# ESTILO DE LA APLICACIÓN #
# ======================= #
st.markdown("""
<style>
.big-title {
    font-size:100px;
    font-weight:700;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p style="font-size:48px; font-weight:800; text-align:center;">🏠 Predicción del Valor de Viviendas</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center; font-size:25px; font-weight:400;">Complete la información para estimar el valor de mercado</p>',
    unsafe_allow_html=True
)

# ============================================= #
# ENTRADAS DE LA BARRA LATERAL (SIDEBAR INPUTS) #
# ============================================= #
st.sidebar.markdown(
    '<p style="font-size:22px; font-weight:700;">📊 Variables de Entrada</p>',
    unsafe_allow_html=True
)

input_data = {}

for col in features:
    
    # Numéricas
    if col in num_cols:
        input_data[col] = st.sidebar.number_input(
            col,
            value=0.0
        )
    
    # Categóricas
    elif col in cat_cols:
        input_data[col] = st.sidebar.selectbox(
            col,
            cat_values[col]
        )

# ===================== #
# PREDICCIÓN DEL MODELO #
# ===================== #
if st.sidebar.button("🔮 Predecir"):
    
    df = pd.DataFrame([input_data])
    
    try:
        pred = model.predict(df)[0]
        
        st.success(f"💰 Valor Estimado: ${pred:,.0f}")
    
    except Exception as e:
        st.error(f"Error en la predicción: {e}")

# ============= #
# MOSTRAR INPUT #
# ============= #

df_input = pd.DataFrame([input_data]).T
df_input.columns = ["Valor"]

styled = df_input.style \
    .set_properties(**{
        'text-align': 'left',
        'font-size': '14px'
    }) \
    .set_table_styles([
        {'selector': 'th', 'props': [('font-weight', 'bold'), ('text-align', 'left')]},
        {'selector': 'td', 'props': [('padding', '6px')]}
    ])

st.markdown(
    '<p style="text-align:center;font-size:22px; font-weight:700;">📄 Datos Ingresados</p>',
    unsafe_allow_html=True
)
st.dataframe(styled)

# ======================================== #
#        Ejecución desde la Terminal       #
# streamlit run src/housing_pred_stream.py #
# ======================================== #
