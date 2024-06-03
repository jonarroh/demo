#!/bin/sh

# Cargar las variables de entorno desde el archivo .env
set -a
. ./.env
set +a

# Verificar el valor de isDev y arrancar el servidor correspondiente
if [ "$isDev" -eq 1 ]; then
    echo "Iniciando el servidor de desarrollo..."
    # Iniciar el servidor de desarrollo
    python3 app.py
else
    echo "Iniciando el servidor de producción..."
    # Iniciar el servidor de producción con Gunicorn
    gunicorn --bind 0.0.0.0:8000 app:app
fi
