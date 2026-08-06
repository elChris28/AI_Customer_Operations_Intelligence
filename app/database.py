""""
=========================================
Conexión a SQL Server
=========================================
"""
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def build_connection_string() -> str:
    """
    Construye la cadena de conexión utilizando variables almacenadas en el archivo .env.
    """

    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

    required_values = {
        "DB_SERVER": server,
        "DB_DATABASE": database,
        "DB_USERNAME": username,
        "DB_PASSWORD": password,
    }

    missing_variables = [
        name
        for name, value in required_values.items()
        if not value
    ]

    if missing_variables:
        missing = ", ".join(missing_variables)

        raise ValueError(
            f"Faltan variables de entorno obligatorias: {missing}"
        )

    return (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
    )


def get_connection() -> pyodbc.Connection:
    """
    Devuelve una conexión activa a SQL Server.
    """

    connection_string = build_connection_string()
    return pyodbc.connect(connection_string)