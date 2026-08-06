"""
==========================================================
AI Customer Operations Intelligence
Módulo: Build Dimensions

Descripción:
Construye las tablas dimensión a partir de los datos procesados.

Autor: Christofer Ynga
==========================================================
"""

from pathlib import Path
import pandas as pd


# RUTAS

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_PATH = BASE_DIR / "data" / "processed"
DW_PATH = BASE_DIR / "data" / "warehouse"
DW_PATH.mkdir(exist_ok=True)

# LEER CONVERSACIONES
conversations = pd.read_csv(
    PROCESSED_PATH / "conversations.csv"
)


dim_canal = (
    conversations[["Canal"]]
    .drop_duplicates()
    .sort_values("Canal")
    .reset_index(drop=True)
)

dim_canal.insert(
    0,
    "CanalID",
    range(1, len(dim_canal) + 1)
)


dim_servicio = (
    conversations[["Servicio"]]
    .drop_duplicates()
    .sort_values("Servicio")
    .reset_index(drop=True)
)

dim_servicio.insert(
    0,
    "ServicioID",
    range(1, len(dim_servicio) + 1)
)


dim_intencion = (
    conversations[["Intencion"]]
    .drop_duplicates()
    .sort_values("Intencion")
    .reset_index(drop=True)
)

dim_intencion.insert(
    0,
    "IntencionID",
    range(1, len(dim_intencion) + 1)
)


# EXPORTAR
dim_canal.to_csv(
    DW_PATH / "DimCanal.csv",
    index=False,
    encoding="utf-8-sig"
)

dim_servicio.to_csv(
    DW_PATH / "DimServicio.csv",
    index=False,
    encoding="utf-8-sig"
)

dim_intencion.to_csv(
    DW_PATH / "DimIntencion.csv",
    index=False,
    encoding="utf-8-sig"
)

print("✓ Dimensiones creadas correctamente")