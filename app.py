import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Analisis de Venta de Carros Usados')

st.write('Esta aplicación muestra la frecuencia la distribución y relación con el precio en los datos de vehículos usados')

hist_button = st.button('Construir histograma según Odómetro') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de venta de vehículos')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", color='condition', nbins=50)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


hist_button = st.button('Construir Gráfico de Dispersión: Odómetro vs. Precio') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de gráfico de dispersión de odómetro vs. precio del vehículo usado.')
         
    # crear gráfico de dispersión
    fig = px.scatter(df_odometer, x="odometer", y="price", color='condition')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)