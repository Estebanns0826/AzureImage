# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos, incluyendo la carpeta templates
COPY . .

# Exponer el puerto
EXPOSE 3500

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
