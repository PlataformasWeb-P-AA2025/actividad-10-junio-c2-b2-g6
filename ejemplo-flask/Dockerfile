# Imagen base de Python
FROM python:3.10

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo app.py al contenedor
COPY app.py .

# Instalar Flask dentro del contenedor
RUN pip install flask

# Exponer el puerto donde Flask se ejecuta
EXPOSE 5000

# Comando para ejecutar tu aplicación Flask
CMD ["python", "app.py"]
