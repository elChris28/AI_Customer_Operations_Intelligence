"""
==========================================================
AI Customer Operations Intelligence
Módulo: ETL Pipeline

Descripción:
Orquesta el flujo completo del proceso ETL.

Extract
↓
Transform
↓
Quality
↓
Processed

Autor: Christofer Ynga
==========================================================
"""

from pathlib import Path

from extract import (
    extract_customers,
    extract_conversations
)

from transform import (
    transform_customers,
    transform_conversations
)

from quality import (
    generate_quality_report,
    save_report
)


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_PATH = BASE_DIR / "data" / "processed"

PROCESSED_PATH.mkdir(exist_ok=True)


def run_pipeline():

    print("=" * 50)
    print("INICIANDO PIPELINE ETL")
    print("=" * 50)

    # EXTRACT
    customers_raw = extract_customers()
    conversations_raw = extract_conversations()

    print("✓ Extract finalizado")


    # TRANSFORM
    customers = transform_customers(
        customers_raw
    )

    conversations = transform_conversations(
        conversations_raw
    )

    print("✓ Transform finalizado")


    # QUALITY
    customers_report = generate_quality_report(
        customers_raw,
        customers,
        "Customers"
    )

    conversations_report = generate_quality_report(
        conversations_raw,
        conversations,
        "Conversations"
    )

    report = customers_report

    report = report._append(
        conversations_report,
        ignore_index=True
    )

    save_report(report)

    print("✓ Reporte de calidad generado")


    # PROCESSED
    customers.to_csv(

        PROCESSED_PATH /
        "customers.csv",

        index=False,

        encoding="utf-8-sig"

    )

    conversations.to_csv(

        PROCESSED_PATH /
        "conversations.csv",

        index=False,

        encoding="utf-8-sig"

    )

    print("✓ Datos procesados guardados")

    print("=" * 50)
    print("PIPELINE FINALIZADO")
    print("=" * 50)


if __name__ == "__main__":

    run_pipeline()