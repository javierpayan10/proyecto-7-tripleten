import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Dashboard de Anuncios de Venta de Coches")

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si se selecciona la casilla
    st.write('Creando un histograma para la columna "odometer"')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # Si se selecciona la casilla
    st.write('Creando un gráfico de dispersión para "price" y "odometer"')
    fig = px.scatter(car_data, x="price", y="odometer", color="condition")
    st.plotly_chart(fig, use_container_width=True)
    
