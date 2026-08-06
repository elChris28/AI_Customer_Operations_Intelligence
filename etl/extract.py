"""
==========================================================
AI Customer Operations Intelligence
Módulo: Extract

Descripción:
Lee los archivos CSV desde la carpeta data/raw y los carga como DataFrames de pandas.

Autor: Christofer Ynga
==========================================================
"""

from pathlib import Path
import pandas as pd

# RUTAS
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "raw"

# FUNCIÓN GENERAL
def read_csv(file_name: str) -> pd.DataFrame:
    """
    Lee un archivo CSV desde la carpeta raw.
    """
    file_path = RAW_PATH / file_name

    if not file_path.exists():

        raise FileNotFoundError(
            f"No existe el archivo: {file_path}"
        )

    return pd.read_csv(file_path)

# CLIENTES
def extract_customers():
    return read_csv("customers.csv")

# CONVERSACIONES
def extract_conversations():
    return read_csv("conversations.csv")


def main():

    customers = extract_customers()
    conversations = extract_conversations()
    print(customers.head())
    print()
    print(conversations.head())


if __name__ == "__main__":
    main()