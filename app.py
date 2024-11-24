import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

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
    


build_bar_chart = st.checkbox('Construir gráfico de barras')

if build_bar_chart:  # Si se hace clic en el botón
    st.write('Creando un gráfico de barras para la distribución de la condición de los vehículos')

    # Calcular la distribución de la condición
    condition_counts = car_data['condition'].value_counts()

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(condition_counts.index, condition_counts.values, color='blue')
    ax.set_title('Distribución de la Condición del Vehículo', fontsize=16)
    ax.set_xlabel('Condición', fontsize=12)
    ax.set_ylabel('Cantidad de Vehículos', fontsize=12)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

build_price_histogram = st.checkbox('Construir histograma de precios')

if build_price_histogram:  # Si se hace clic en el botón
    st.write("Distribución de los precios de los vehículos")
    
    # Crear el histograma
    fig = px.histogram(
        car_data,
        x='price',
        nbins=30,  # Número de bins en el histograma
        title='Distribución de Precios de Vehículos',
        labels={'price': 'Precio (USD)'},
        template='plotly_white'
    )
    
    # Mejorar el diseño del gráfico
    fig.update_layout(
        xaxis_title="Precio (USD)",
        yaxis_title="Cantidad de Vehículos",
        bargap=0.2
    )
    
    # Mostrar el histograma en Streamlit
    st.plotly_chart(fig, use_container_width=True)