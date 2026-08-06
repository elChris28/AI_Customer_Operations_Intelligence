"""
==========================================================
AI Customer Operations Intelligence
Módulo: Transform

Descripción:
Realiza la limpieza y transformación de los datos extraídos desde la capa RAW.

Autor: Christofer Ynga
==========================================================
"""

import pandas as pd

# CLIENTES
# ==========================================================

def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y transforma la tabla de clientes.
    """
    df = df.copy()
    # Eliminar duplicados
    df = df.drop_duplicates(subset=["ClienteID"])
    # Eliminar nombres nulos
    df = df.dropna(subset=["Nombre"])

    # Edad válida
    df = df[
        (df["Edad"] >= 18) &
        (df["Edad"] <= 70)
    ]

    # Distrito nulo
    df["Distrito"] = df["Distrito"].fillna(
        "No especificado"
    )

    # Tipo cliente nulo
    df["TipoCliente"] = df["TipoCliente"].fillna(
        "Nuevo"
    )

    # Limpiar espacios
    df["Nombre"] = df["Nombre"].str.strip()

    return df

# CONVERSACIONES
# ==========================================================

def transform_conversations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y transforma la tabla de conversaciones.
    """

    df = df.copy()

    # Eliminar ConversationID duplicados
    df = df.drop_duplicates(
        subset=["ConversationID"]
    )

    # Convertir fecha
    df["FechaHora"] = pd.to_datetime(
        df["FechaHora"],
        errors="coerce"
    )

    # Eliminar fechas inválidas
    df = df.dropna(subset=["FechaHora"])

    # Duración válida
    df = df[
        df["DuracionMinutos"] > 0
    ]

    # Limpiar espacios
    columnas_texto = [
        "Canal",
        "Intencion",
        "Servicio",
        "EstadoConversacion"
    ]

    for columna in columnas_texto:

        df[columna] = (
            df[columna]
            .astype(str)
            .str.strip()
        )

    return df