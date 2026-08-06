"""
==========================================================
AI Customer Operations BI
Módulo: Load
Descripción:
Carga las tablas del Data Warehouse en SQL Server.
==========================================================
"""

from pathlib import Path
import pandas as pd
import pyodbc

from config import CONNECTION_STRING


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED = BASE_DIR / "data" / "processed"
WAREHOUSE = BASE_DIR / "data" / "warehouse"


# CONEXIÓN
# ==========================================

def get_connection():
    return pyodbc.connect(CONNECTION_STRING)

# CARGA DE TABLA
# ==========================================

def load_table(csv_path, table_name):

    df = pd.read_csv(csv_path)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.fast_executemany = True
    columns = ",".join(df.columns)

    placeholders = ",".join(["?"] * len(df.columns))

    sql = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES ({placeholders})
    """

    try:
        cursor.executemany(
            sql,
            df.values.tolist()
        )

        connection.commit()
        print(f"✓ {table_name}: {len(df)} registros cargados.")

    except Exception as e:

        connection.rollback()
        print(f"X Error en {table_name}")
        print(e)

    finally:

        cursor.close()
        connection.close()


# MAIN
# ==========================================
def main():

    print("="*50)
    print("CARGANDO DATA WAREHOUSE")
    print("="*50)

    load_table(
        PROCESSED/"customers.csv",
        "DimCliente"
    )

    load_table(
        WAREHOUSE/"DimFecha.csv",
        "DimFecha"
    )

    load_table(
        WAREHOUSE/"DimCanal.csv",
        "DimCanal"
    )

    load_table(
        WAREHOUSE/"DimServicio.csv",
        "DimServicio"
    )

    load_table(
        WAREHOUSE/"DimIntencion.csv",
        "DimIntencion"
    )

    load_table(
        WAREHOUSE/"FactConversaciones.csv",
        "FactConversaciones"
    )

    print("="*50)
    print("DATA WAREHOUSE CARGADO")
    print("="*50)


if __name__ == "__main__":
    main()