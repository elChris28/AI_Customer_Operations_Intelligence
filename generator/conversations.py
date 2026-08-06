"""
==========================================================
AI Customer Operations Intelligence
Archivo: conversations.py

Descripción:
Genera conversaciones sintéticas simulando la operación de un chatbot empresarial.

Autor: Christofer Ynga
==========================================================
"""

import random
from datetime import datetime, timedelta
import pandas as pd

from config import (
    CHANNELS,
    CHANNEL_WEIGHTS,
    INTENTS,
    INTENT_DURATION_RULES,
    INTENT_ERROR_PROBABILITY,
    SERVICES,
    STATUS,
    STATUS_WEIGHTS,
    BASE_CONVERSION_PROBABILITY,
    CHANNEL_CONVERSION_MODIFIER,
    TOTAL_CONVERSATIONS
)

def generate_duration(intent):
    """
    Genera la duración de una conversación según la intención.
    """

    minimum, maximum = INTENT_DURATION_RULES[intent]
    return random.randint(minimum, maximum)


def generate_datetime():
    """
    Genera una fecha y hora aleatoria durante el año 2025.
    Las conversaciones tienen mayor probabilidad de ocurrir en horarios de mayor demanda.
    """

    start_date = datetime(2025, 1, 1)
    random_days = random.randint(0, 364)
    date = start_date + timedelta(days=random_days)

    period = random.choices(
        ["peak", "normal", "night"],
        weights=[0.70, 0.20, 0.10],
        k=1
    )[0]

    if period == "peak":

        hour = random.choice(
            [12, 13, 18, 19, 20]
        )

    elif period == "normal":

        hour = random.choice(
            [8, 9, 10, 11, 15, 16, 17]
        )

    else:

        hour = random.choice(
            [0, 1, 2, 3, 4, 5]
        )

    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    return date.replace(
        hour=hour,
        minute=minute,
        second=second
    )

def generate_conversion(customer_type, channel, status):
    """
    Determina si una conversación termina en conversión.
    """

    # Si el cliente abandonó la conversación,
    # no puede convertirse.

    if status == "Abandonada":
        return False

    probability = (
        BASE_CONVERSION_PROBABILITY[customer_type]
        + CHANNEL_CONVERSION_MODIFIER[channel]
    )

    probability = max(0,min(probability,1))

    return random.random() < probability


def generate_chatbot_error(intent):

    probability = INTENT_ERROR_PROBABILITY[intent]
    return random.random() < probability


def generate_satisfaction(status, has_error, converted):

    if status == "Abandonada":
        return random.choice([1, 1, 2])

    if has_error:
        return random.choice([1, 2, 2, 3])

    if converted:
        return random.choice([4, 5, 5, 5])
    
    return random.choice([3, 3, 4, 4, 5])



def generate_conversations(customers_df):

    conversations = []

    for conversation_id in range(1, TOTAL_CONVERSATIONS + 1):

        customer = customers_df.sample(1).iloc[0]
        channel = random.choices(
            CHANNELS,
            weights=CHANNEL_WEIGHTS,
            k=1
        )[0]

        intent = random.choice(INTENTS)
        service = random.choice(SERVICES)
        status = random.choices(
            STATUS,
            weights=STATUS_WEIGHTS,
            k=1
        )[0]

        date_time = generate_datetime()
        duration = generate_duration(intent)
        has_error = generate_chatbot_error(intent)
        converted = generate_conversion(
            customer["TipoCliente"],
            channel,
            status
        )

        satisfaction = generate_satisfaction(
            status,
            has_error,
            converted
        )

        conversation = {
            "ConversationID": conversation_id,
            "ClienteID": customer["ClienteID"],
            "FechaHora": date_time,
            "Canal": channel,
            "Intencion": intent,
            "Servicio": service,
            "DuracionMinutos": duration,
            "TuvoError": has_error,
            "EstadoConversacion": status,
            "Convertido": converted,
            "Satisfaccion": satisfaction
        }

        conversations.append(conversation)

    return pd.DataFrame(conversations)
