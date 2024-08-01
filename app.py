import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", color="blue", title="Odometer vs Price by Year")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# Mostrar el histograma si se selecciona la casilla de verificación correspondiente
if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    hist_fig = px.histogram(car_data, x="odometer", title="Histograma del odómetro")
    st.plotly_chart(hist_fig, use_container_width=True)

# Mostrar el gráfico de dispersión si se selecciona la casilla de verificación correspondiente
if show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    scatter_fig = px.scatter(car_data, x="odometer", y="price", color="blue", title="Odometer vs Price by Year")
    st.plotly_chart(scatter_fig, use_container_width=True)
