# Predictor de Eficiencia PTAP

Aplicación web desarrollada con Streamlit para predecir la eficiencia de una Planta de Tratamiento de Agua Potable (PTAP) basada en variables de entrada como Turbidez, pH y Caudal.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio o descargar los archivos
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```
2. Abrir el navegador en http://localhost:8501
3. Cargar un archivo CSV con las siguientes columnas:
   - Turbidez_Entrada
   - pH_Entrada
   - Caudal

## Estructura del Proyecto

```
├── app.py                 # Aplicación principal
├── modelo.py              # Script de entrenamiento del modelo
├── regre_ptap.pkl        # Modelo entrenado
├── requirements.txt       # Dependencias del proyecto
├── Data/                  # Directorio de datos
└── Images/               # Directorio de imágenes
```

## Despliegue en Streamlit Cloud

1. Crear una cuenta en [Streamlit Cloud](https://streamlit.io/cloud)
2. Conectar con el repositorio de GitHub
3. Seleccionar el archivo app.py como punto de entrada
4. La aplicación se desplegará automáticamente

## Notas

- El archivo CSV debe usar punto y coma (;) como separador
- Asegurarse de que las columnas tengan los nombres exactos especificados