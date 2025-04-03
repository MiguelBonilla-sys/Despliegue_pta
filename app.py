from turtle import up
import streamlit as st
import pandas as pd
import pickle
from PIL import Image

st.title("Predictor de Eficiencia PTAP")
st.write("A partir de las variables de entrada a continuacion se muestra la eficiencia PTAP del material. ")
logo = Image.open(r"Images\logo_usb.png")

st.sidebar.header("Cargue un archivo csv con las variables Turbidez, Phy caudal.")
st.sidebar.image(logo)
st.sidebar.header("Cargue un archivo csv con las variables Turbidez, Phy caudal.")
st.subheader("Prediccion eficiencia PTAP")

uploaded_file = st.sidebar.file_uploader("Cargar archivo", type=["csv"])
if uploaded_file is not None:
    input_dfd = pd.read_csv(uploaded_file,sep=";")
    load_pred = pickle.load(open('regre_ptap.pkl','rb'))
    input_dfd['estimacion_efi'] = load_pred.predict(input_dfd)
    st.write(input_dfd)