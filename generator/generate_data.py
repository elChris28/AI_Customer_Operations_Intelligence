"""
==========================================================
AI Customer Operations Intelligence
Archivo: generate_data.py

Orquesta la generación de datos sintéticos.
==========================================================
"""

import os
from customers import generate_customers
from conversations import generate_conversations


def main():

    print("Generando clientes...")

    customers_df = generate_customers(2000)

    os.makedirs("../data/raw", exist_ok=True)

    customers_df.to_csv(
        "../data/raw/customers.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("Clientes generados correctamente.")

    print("Generando conversaciones...")

    conversations_df = generate_conversations(customers_df)

    conversations_df.to_csv(
        "../data/raw/conversations.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("Conversaciones generadas correctamente.")

    print(f"Total clientes: {len(customers_df):,}")

    print(f"Total conversaciones: {len(conversations_df):,}")


if __name__ == "__main__":
    main()