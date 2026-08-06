"""
==========================================================
AI Customer Operations Intelligence
Módulo: Build Fact Table
==========================================================
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED = BASE_DIR / "data" / "processed"
WAREHOUSE = BASE_DIR / "data" / "warehouse"


# LEER ARCHIVOS

conversations = pd.read_csv(PROCESSED / "conversations.csv")

dim_canal = pd.read_csv(WAREHOUSE / "DimCanal.csv")
dim_servicio = pd.read_csv(WAREHOUSE / "DimServicio.csv")
dim_intencion = pd.read_csv(WAREHOUSE / "DimIntencion.csv")

dim_fecha = pd.read_csv(
    WAREHOUSE / "DimFecha.csv"
)

conversations["FechaHora"] = pd.to_datetime(conversations["FechaHora"])
conversations["Fecha"] = conversations["FechaHora"].dt.normalize()

dim_fecha["Fecha"] = pd.to_datetime(dim_fecha["Fecha"])

# REEMPLAZAR TEXTO POR IDs

fact = conversations.merge(
    dim_fecha,
    on="Fecha",
    how="left"
)

fact = fact.merge(
    dim_canal,
    on="Canal",
    how="left"
)

fact = fact.merge(
    dim_servicio,
    on="Servicio",
    how="left"
)

fact = fact.merge(
    dim_intencion,
    on="Intencion",
    how="left"
)

# ELIMINAR COLUMNAS TEXTO
fact = fact.drop(
    columns=[
        "Canal",
        "Servicio",
        "Intencion",
        "Fecha"
    ]
)


# REORDENAR
fact = fact[[
    "ConversationID",
    "ClienteID",
    "FechaID",
    "CanalID",
    "ServicioID",
    "IntencionID",
    "DuracionMinutos",
    "TuvoError",
    "EstadoConversacion",
    "Convertido",
    "Satisfaccion"
]]


# EXPORTAR

fact.to_csv(
    WAREHOUSE / "FactConversaciones.csv",
    index=False,
    encoding="utf-8-sig"
)

print("✓ FactConversaciones creada")