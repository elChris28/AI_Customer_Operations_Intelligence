"""
==========================================================
AI Customer Operations Intelligence
Módulo: Quality

Descripción:
Calcula métricas de calidad de datos y genera un reporte CSV para el proceso ETL.

Autor: Christofer Ynga
==========================================================
"""

from pathlib import Path
from datetime import datetime
import pandas as pd

# RUTAS
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_PATH = BASE_DIR / "reports"
REPORTS_PATH.mkdir(exist_ok=True)

# CALIDAD
# ==========================================================

def generate_quality_report(
    original_df: pd.DataFrame,
    transformed_df: pd.DataFrame,
    table_name: str
) -> pd.DataFrame:

    original_rows = len(original_df)

    final_rows = len(transformed_df)

    removed_rows = original_rows - final_rows

    duplicated = original_df.duplicated().sum()

    null_values = original_df.isnull().sum().sum()

    quality_score = (
        (final_rows / original_rows) * 100
        if original_rows > 0 else 0
    )

    report = pd.DataFrame([{

        "Tabla": table_name,

        "FechaEjecucion":
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "RegistrosOriginales":
        original_rows,

        "RegistrosFinales":
        final_rows,

        "RegistrosEliminados":
        removed_rows,

        "DuplicadosDetectados":
        duplicated,

        "ValoresNulos":
        null_values,

        "DataQualityScore":
        round(quality_score,2)

    }])

    return report

# EXPORTAR
# ==========================================================

def save_report(report: pd.DataFrame):

    file_name = (
        "data_quality_report.csv"
    )

    report.to_csv(
        REPORTS_PATH / file_name,
        index=False,
        encoding="utf-8-sig"
    )