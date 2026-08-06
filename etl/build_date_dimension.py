"""
==========================================================
AI Customer Operations Intelligence
Módulo: Build Date Dimension
==========================================================
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED = BASE_DIR / "data" / "processed"
WAREHOUSE = BASE_DIR / "data" / "warehouse"

# Leer conversaciones
df = pd.read_csv(PROCESSED / "conversations.csv")

# Convertir a fecha
df["FechaHora"] = pd.to_datetime(df["FechaHora"])

# Crear solo la fecha (sin hora)
df["Fecha"] = df["FechaHora"].dt.date

# Crear dimensión
dim_fecha = (
    df[["Fecha"]]
    .drop_duplicates()
    .sort_values("Fecha")
    .reset_index(drop=True)
)

# Clave sustituta
dim_fecha.insert(0, "FechaID", range(1, len(dim_fecha) + 1))

# Atributos de tiempo
dim_fecha["Fecha"] = pd.to_datetime(dim_fecha["Fecha"])
dim_fecha["Anio"] = dim_fecha["Fecha"].dt.year
dim_fecha["Mes"] = dim_fecha["Fecha"].dt.month

# Diccionario de meses en español
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

dim_fecha["NombreMes"] = dim_fecha["Mes"].map(meses)
dim_fecha["Trimestre"] = dim_fecha["Fecha"].dt.quarter
dim_fecha["Dia"] = dim_fecha["Fecha"].dt.day

dias = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

dim_fecha["DiaSemana"] = (dim_fecha["Fecha"].dt.day_name().map(dias))
dim_fecha["Semana"] = (dim_fecha["Fecha"].dt.isocalendar().week.astype(int))

dim_fecha.to_csv(
    WAREHOUSE / "DimFecha.csv",
    index=False,
    encoding="utf-8-sig"
)

print("✓ DimFecha creada correctamente")