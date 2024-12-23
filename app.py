import streamlit as st
import pandas as pd
import sidetable as stb
import plotly.express as px

st.title("_Esta es la presentacion del proyecto_ :bar_chart: del Spring 7")
st.title("Realizado por :green[Carlos Zeballos] 💻")

st.write(':blue[Presentacion de los datos inicial]')
car_data = pd.read_csv('vehicles_us.csv')
st.dataframe(car_data)

st.write(':blue[Revisamos las primeras filas]')
st.dataframe(car_data.head())

st.write(':blue[Revisamos valores ausentes]')
st.dataframe(car_data.stb.missing(style=True))

boton_histograma= st.button('Crear Histograma del comportamiento del odometro ', type='primary')
# creamos un histograma
if boton_histograma:
    fig_histograma = px.histogram(car_data, x='odometer', nbins=50)
    st.plotly_chart(fig_histograma)

boton_dispersion = st.button('Crear dispersion del comportamiento del odometro y precio', type='primary')
# creamos un diagrama de dispersion
if boton_dispersion:
    fig_dispersion = px.scatter(car_data, x='odometer', y ='price')
    st.plotly_chart(fig_dispersion)


