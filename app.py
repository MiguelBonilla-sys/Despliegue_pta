import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import os

# Configuración de la página
st.set_page_config(
    page_title="Predictor de Eficiencia PTAP",
    page_icon="🌊",
    layout="wide"
)

# Título y descripción
st.title("Predictor de Eficiencia PTAP")
st.write("A partir de las variables de entrada a continuación se muestra la eficiencia PTAP del material.")

# Configuración de la barra lateral
try:
    logo = Image.open(os.path.join("Images", "logo_usb.png"))
    st.sidebar.image(logo)
except Exception as e:
    st.sidebar.warning("No se pudo cargar el logo")

st.sidebar.header("Cargue un archivo CSV con las variables")
st.sidebar.write("El archivo debe contener las columnas: Turbidez, pH y Caudal")

# Carga y procesamiento del archivo
uploaded_file = st.sidebar.file_uploader("Cargar archivo", type=["csv"])
if uploaded_file is not None:
    try:
        input_dfd = pd.read_csv(uploaded_file, sep=";")
        required_columns = ["Turbidez_Entrada", "pH_Entrada", "Caudal"]
        
        if all(col in input_dfd.columns for col in required_columns):
            with open('regre_ptap.pkl', 'rb') as model_file:
                load_pred = pickle.load(model_file)
            
            input_dfd['Eficiencia_Estimada'] = load_pred.predict(input_dfd)
            
            st.subheader("Resultados de la Predicción")
            st.dataframe(input_dfd.style.highlight_max(axis=0))
            
            # Mostrar estadísticas básicas
            st.subheader("Estadísticas de la Predicción")
            st.write(input_dfd['Eficiencia_Estimada'].describe())
        else:
            st.error("El archivo CSV debe contener las columnas: Turbidez_Entrada, pH_Entrada y Caudal")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {str(e)}")

# Información adicional
st.sidebar.markdown("---")
st.sidebar.info("Desarrollado por USB")