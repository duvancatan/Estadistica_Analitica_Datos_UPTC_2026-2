import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# =========================
# KPIs
# =========================

mainpath= "/Users/duvancatano/Documents/Estadistica_Analitica_Datos_UTPC_2026-1/data/housing"
filename= "housing_dataset.csv"
fullpath= os.path.join(mainpath,filename)
df = pd.read_csv(fullpath, sep=",") # El separador es "," porque en el archivo .csv los valores están separados por coma
pd.set_option('display.max_columns', None) # Para mostrar todas las columnas del DataFrame sin truncar


kpi_valor_promedio = df["valor_de_mercado_de_la_vivienda"].mean()
kpi_area_promedio = df["area_total_m2"].mean()
kpi_ingreso_promedio = df["ingreso_del_hogar"].mean()

# =============================================== #
# FIGURA 1: Scatter de Área vs Valor por Estrato  #
# =============================================== #

fig1 = px.scatter(
    df,
    x="area_total_m2",
    y="valor_de_mercado_de_la_vivienda",
    color="estrato",
    hover_data=["municipio"],
    title= "Relación Área vs Valor de Vivienda"
)

# ======================================= #
# FIGURA 2: Boxplot del Valor por Estrato #
# ======================================= #

fig2 = px.box(
    df,
    x="estrato",
    y="valor_de_mercado_de_la_vivienda",
    title= "Distribución del Valor por Estrato"
)

# ================================ #
# FIGURA 3: Histograma de Ingresos #
# ================================ #

fig3 = px.histogram(
    df,
    x="ingreso_del_hogar",
    nbins=50,
    title="Distribución del Ingreso del Hogar"
)

# ================================ #
# FIGURA 4: Promedio por Municipio #
# ================================ #

fig4 = px.scatter(
    df,
    x="ingreso_del_hogar",
    y="valor_de_mercado_de_la_vivienda",
    color="estrato",
    hover_data=["municipio"],
    title="Relación de Ingreso vs Valor de Vivienda"
)

# ============================================== #
# FIGURA 5: Distribución de Ingresos por Estrato #
# ============================================== #

fig5 = px.box(
    df,
    x="estrato",
    y="ingreso_del_hogar",
    title="Distribución del Ingrersos por Estrato"
)

# ========================================== #
# FIGURA 6: Relación de Pobreza con Ingresos #
# ========================================== #

fig6 = px.scatter(
    df,
    x="indice_de_pobreza",
    y="ingreso_del_hogar",
    color="municipio",
    hover_data=["estrato"],
    title="Relación Área vs Valor de Vivienda"
)


# =========================
# GENERAR HTML
# =========================

with open("dashboard_housing.html", "w") as f:
    
    f.write(f"""
    <html>
    <head>
        <title>Dashboard Ejecutivo</title>
    </head>
    <body style="font-family: Arial; margin:40px">
    
    <h1>📊 Dashboard de Colombia Housing & Income Dataset </h1>
    
    <h2>Indicadores Generales</h2>
    <ul>
        <li><b>Valor promedio:</b> {kpi_valor_promedio:,.2f}</li>
        <li><b>Área promedio:</b> {kpi_area_promedio:,.2f}</li>
        <li><b>Ingreso promedio:</b> {kpi_ingreso_promedio:,.2f}</li>
    </ul>
    
    <h2>📈 Área vs Valor</h2>
    {fig1.to_html(full_html=False)}
    
    <h2>📦 Valor por Estrato</h2>
    {fig2.to_html(full_html=False)}
    
    <h2>💰 Distribución de Ingresos</h2>
    {fig3.to_html(full_html=False)}
    
    <h2>🛖 Relación de Ingresos con Valor de Vivienda</h2>
    {fig4.to_html(full_html=False)}
    
    <h2>💸 Relación de Ingresos por Estrato</h2>
    {fig5.to_html(full_html=False)}
    
    <h2>🗑️ Relación de Pobreza con Ingresos</h2>
    {fig6.to_html(full_html=False)}
    
    </body>
    </html>
    """)

print("✅ Dashboard generado: dashboard_ejecutivo.html")


# ============================ #
# Ejecución desde la Terminal  #
#  python3 src/housing_eda.py  # 
# ============================ #
