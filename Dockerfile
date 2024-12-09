# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app/LLM_Vitta

# Copiar primero solo los archivos necesarios para instalar dependencias
COPY setup.py .
COPY README.md .

# Copiar el resto del proyecto incluyendo el .env
COPY llm_project/ ./llm_project/

# Instalar dependencias
RUN pip install --no-cache-dir -e .

# Exponer el puerto que usa Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "llm_project/src/frontend/app.py", "--server.address=0.0.0.0"] 