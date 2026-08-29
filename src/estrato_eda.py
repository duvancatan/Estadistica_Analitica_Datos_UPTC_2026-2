#================================================#
# LIBRERÍAS
#================================================#

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
# pip install streamlit plotly pandas numpy

#================================================#
# CONFIGURACIÓN
#================================================#

st.set_page_config(
    page_title="EDA Viviendas",
    layout="wide"
)

#================================================#
# CARGAR DATOS
#================================================#

# Reemplace con su archivo
#mainpath= "/Users/duvancatano/Documents/Estadistica_Analitica_Datos_UTPC_2026-1/data/housing/housing_dataset.csv"
data = pd.read_csv("/Users/duvancatano/Documents/Estadistica_Analitica_Datos_UPTC_2026-2/data/housing/housing_dataset.csv")

#================================================#
# TÍTULO
#================================================#

st.title("🏠 EDA Interactivo por Estrato")

st.markdown(
    "Análisis descriptivo interactivo filtrando por estrato."
)

#================================================#
# SIDEBAR
#================================================#

st.sidebar.header("Filtros")

estrato = st.sidebar.selectbox(
    "Seleccione el estrato",
    sorted(data["estrato"].dropna().unique())
)

#================================================#
# FILTRAR DATOS
#================================================#

df = data[
    data["estrato"] == estrato
]

#================================================#
# MÉTRICAS PRINCIPALES
#================================================#

st.subheader(f"Indicadores principales - Estrato {estrato}")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Viviendas",
    len(df)
)

col2.metric(
    "Área promedio",
    f"{df['area_total_m2'].mean():.2f} m²"
)

col3.metric(
    "Habitaciones promedio",
    f"{df['habitaciones'].mean():.2f}"
)

col4.metric(
    "Ingreso promedio",
    f"${df['ingreso_del_hogar'].mean():,.0f}"
)

#================================================#
# ESTADÍSTICAS DESCRIPTIVAS
#================================================#

st.subheader("📊 Estadísticas descriptivas")

desc = (
    df
    .describe()
    .round(2)
)

st.dataframe(
    desc,
    use_container_width=True
)

#================================================#
# HEATMAP CORRELACIÓN
#================================================#

st.subheader("🔥 Matriz de correlación")

corr = (
    df
    .select_dtypes(include=np.number)
    .corr()
)

fig_corr = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    color_continuous_midpoint=0
)

fig_corr.update_layout(
    template="plotly_white",
    height=700
)

st.plotly_chart(
    fig_corr,
    use_container_width=True
)

#================================================#
# VARIABLES NUMÉRICAS
#================================================#

st.subheader("📈 Distribuciones numéricas")

vars_num = [
    'area_total_m2',
    'habitaciones',
    'ingreso_del_hogar',
    'valor_de_mercado_de_la_vivienda'
]

var_num = st.selectbox(
    "Seleccione variable numérica",
    vars_num
)

fig_hist = px.histogram(
    df,
    x=var_num,
    nbins=40,
    marginal="box",
    opacity=0.80
)

fig_hist.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

#================================================#
# VARIABLES CATEGÓRICAS
#================================================#

st.subheader("📊 Distribuciones categóricas")

vars_cat = [
    'tipo_de_vivienda',
    'zona_urbana_rural',
    'calidad_de_construccion'
]

var_cat = st.selectbox(
    "Seleccione variable categórica",
    vars_cat
)

freq = (
    df[var_cat]
    .value_counts()
    .reset_index()
)

freq.columns = [var_cat, "Frecuencia"]

fig_bar = px.bar(
    freq,
    x=var_cat,
    y="Frecuencia",
    text_auto=True
)

fig_bar.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

#================================================#
# BOXPLOT
#================================================#

st.subheader("📦 Boxplot por estrato")

fig_box = px.box(
    df,
    y="valor_de_mercado_de_la_vivienda",
    points="outliers"
)

fig_box.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(
    fig_box,
    use_container_width=True
)

#================================================#
# FINAL
#================================================#

st.success(
    "EDA interactivo cargado correctamente."
)


# ================================= #
#    EJECUTAR DESDE LA TERMINAL     #
# streamlit run src/estrato_eda.py  #
# ================================= #