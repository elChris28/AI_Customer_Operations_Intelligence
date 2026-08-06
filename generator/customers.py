"""
==========================================================
AI Customer Operations Intelligence
Archivo: customers.py

Descripción:
Genera clientes sintéticos para el proyecto AI Customer Operations Intelligence.

Autor: Christofer Ynga
==========================================================
"""

from faker import Faker
import random
import pandas as pd
import os

from config import (
    DISTRICTS,
    GENDERS,
    CUSTOMER_TYPES,
    CUSTOMER_TYPE_WEIGHTS
)

# Inicializar Faker
fake = Faker("es_ES")


def generate_customers(total_customers: int) -> pd.DataFrame:
    """
    Genera un DataFrame con clientes sintéticos.

    Parámetros
    ----------
    total_customers : int
        Cantidad de clientes a generar.

    Retorna
    -------
    pandas.DataFrame
        Tabla con los clientes generados.
    """

    customers = []

    for customer_id in range(1, total_customers + 1):

        customer = {
            "ClienteID": customer_id,
            "Nombre": fake.name(),
            "Edad": random.randint(18, 70),
            "Genero": random.choice(GENDERS),
            "Distrito": random.choice(DISTRICTS),
            "TipoCliente": random.choices(
                CUSTOMER_TYPES,
                weights=CUSTOMER_TYPE_WEIGHTS,
                k=1
            )[0]
        }
        customers.append(customer)

    return pd.DataFrame(customers)


def main():

    df_customers = generate_customers(100)
    print(df_customers.head())

    # Crear la carpeta de destino si no existe y guardar el archivo
    os.makedirs("../data/raw", exist_ok=True)
    df_customers.to_csv(
        "../data/raw/customers.csv",
        index=False,
        encoding="utf-8-sig"
    )
    print("Archivo customers.csv generado correctamente.")


if __name__ == "__main__":
    main()