# ======== #
# LBRERÍAS #
# ======== #

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ============= #
# CONFIGURACIÓN #
# ============= #

st.set_page_config(
    page_title="Fraud EDA Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("🥷🏾 Dashboard Analítico de Detección de Fraude Financiero")
st.markdown("Análisis exploratorio interactivo del fraude")

# ===== #
# DATOS #
# ===== #

@st.cache_data
def load_data():
    return pd.read_csv("/Users/duvancatano/Documents/Estadistica_Analitica_Datos_UPTC_2026-2/data/fraud/data_full.csv")

df = load_data()

# ======= #
# SIDEBAR #
# ======= #

st.sidebar.header("🔎 Filtros")

sexo = st.sidebar.multiselect(
    "Sexo",
    df["SEXO"].dropna().unique(),
    default=df["SEXO"].dropna().unique()
)

segmento = st.sidebar.multiselect(
    "Segmento",
    df["SEGMENTO"].dropna().unique(),
    default=df["SEGMENTO"].dropna().unique()
)

edad = st.sidebar.slider(
    "Edad",
    int(df["EDAD"].min()),
    int(df["EDAD"].max()),
    (25, 65)
)

df = df[
    (df["SEXO"].isin(sexo)) &
    (df["SEGMENTO"].isin(segmento)) &
    (df["EDAD"].between(*edad))
]

# ==== #
# KPIs #
# ==== #

col1, col2, col3, col4 = st.columns(4)

col1.metric("Transacciones", len(df))
col2.metric("Fraude %", f"{df['FRAUDE'].mean()*100:.2f}")
col3.metric("Valor medio", f"{df['VALOR'].mean():,.0f}")
col4.metric("Edad media", f"{df['EDAD'].mean():.1f}")

# ============== #
# GRID PRINCIPAL #
# ============== #

c1, c2, c3 = st.columns(3)


# Balance fraude
with c1:
    fig = px.pie(
        df,
        names="FRAUDE",
        title="Distribución Fraude",
        hole=0.5
    )
    fig.update_layout(height=300, margin=dict(l=10,r=10,t=40,b=10))
    st.plotly_chart(fig, use_container_width=True)


# 3. Hora
with c3:
    temp = df.groupby("HORA_AUX")["FRAUDE"].mean().reset_index()
    
    fig = px.line(
        temp,
        x="HORA_AUX",
        y="FRAUDE",
        title="Fraude por hora"
    )
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# ============ #
# SEGUNDA FILA #
# ============ #

c4, c5, c6 = st.columns(3)

# Día semana
with c4:
    # Orden correcto
    orden_dias = [
        "Domingo", "Lunes", "Martes",
        "Miercoles", "Jueves", "Viernes", "Sabado"
    ]

    # Asegurar tipo categórico ordenado
    df["DIASEM"] = pd.Categorical(
        df["DIASEM"],
        categories=orden_dias,
        ordered=True
    )

    # Agrupar
    temp = df.groupby("DIASEM")["FRAUDE"].mean().reset_index()

    # Gráfico
    fig = px.bar(
        temp,
        x="DIASEM",
        y="FRAUDE",
        title="Fraude por día"
    )

    fig.update_layout(height=300)

    st.plotly_chart(fig, use_container_width=True)

# Quincena  
with c5:
    temp = df.groupby("QUINCENA")["FRAUDE"].mean().reset_index()

    fig = px.bar(
        temp,
        x="QUINCENA",
        y="FRAUDE",
        color="FRAUDE",
        color_continuous_scale="Reds",
        title="Fraude por quincena",
        text_auto=".2f"
    )

    fig.update_layout(height=300)

    st.plotly_chart(fig, use_container_width=True) 

# Canal
with c6:
    temp = df.groupby("CANAL")["FRAUDE"].mean().reset_index()

    fig = px.bar(
        temp,
        x="CANAL",
        y="FRAUDE",
        title="Fraude por canal"
    )
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# ============ #
# TERCERA FILA #
# ============ #

c7, c8 = st.columns(2)

# Edad
with c7:
    fig = px.histogram(
        df,
        x="EDAD",
        color="FRAUDE",
        nbins=30,
        title="Edad vs fraude",
        barmode="overlay"
    )
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# Finanzas
with c8:
    fig = px.scatter(
        df,
        x="INGRESOS",
        y="EGRESOS",
        color="FRAUDE",
        title="Ingresos vs Egresos",
        opacity=0.6
    )
    fig.update_xaxes(type="log")
    fig.update_yaxes(type="log")
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# ========= #
# MOVILIDAD #
# ========= #

st.subheader("🌍 Movilidad")

fig = px.scatter(
    df,
    x="Dist_Sum_INTER",
    y="NROPAISES",
    color="FRAUDE",
    opacity=0.5,
    title="Movilidad internacional"
)

fig.update_layout(height=350)

st.plotly_chart(fig, use_container_width=True)

# ====== #
# FOOTER #
# ====== #

st.markdown("---")
st.caption("EDA interactivo para detección de fraude - UdeA")


## ======================================== #
##        Ejecución desde la Terminal       #
##       streamlit run src/fraud_eda.py     #
## ======================================== #