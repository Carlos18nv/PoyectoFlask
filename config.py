"""
config.py
─────────
Configuración central de la aplicación. Lee las variables de entorno
desde el archivo .env para no dejar contraseñas escritas directamente
en el código.
"""

import os
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env al entorno de Python
load_dotenv()


class Config:
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres123")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "tienda_online")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Desactiva una función de SQLAlchemy que no se usa
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para sesiones de Flask 
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-de-desarrollo-temporal")
