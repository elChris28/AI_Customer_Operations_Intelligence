"""
==========================================================
Configuración del proyecto ETL
Las credenciales de SQL Server se cargan desde variables de entorno para evitar publicarlas en GitHub.
==========================================================
"""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# SQL SERVER
SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")


required_values = {
    "DB_SERVER": SERVER,
    "DB_DATABASE": DATABASE,
    "DB_USERNAME": USERNAME,
    "DB_PASSWORD": PASSWORD,
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


CONNECTION_STRING = (
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)