"""
==========================================================
AI Customer Operations Intelligence
Archivo: config.py

Descripción:
Este archivo centraliza toda la configuración utilizada por el generador de datos sintéticos.

Aquí se definen:

- Canales de atención
- Intenciones
- Servicios
- Distritos
- Tipos de clientes
- Probabilidades de negocio

De esta forma evitamos duplicar información en distintos archivos del proyecto.
==========================================================
"""

# ======================================================
# CANALES DE ATENCIÓN
# ======================================================

CHANNELS = [
    "WhatsApp",
    "Web",
    "Facebook",
    "Instagram",
    "Telegram"
]

# Probabilidad de que una conversación llegue por cada canal
CHANNEL_WEIGHTS = [
    0.45,
    0.25,
    0.15,
    0.10,
    0.05
]


# ======================================================
# INTENCIONES DEL CLIENTE
# ======================================================

INTENTS = [
    "Consultar precios",
    "Solicitar información",
    "Agendar servicio",
    "Cancelar servicio",
    "Seguimiento",
    "Reclamo",
    "Soporte técnico"
]

INTENT_DURATION_RULES = {
    "Consultar precios": (3, 5),
    "Solicitar información": (4, 6),
    "Agendar servicio": (5, 8),
    "Cancelar servicio": (2, 4),
    "Seguimiento": (4, 7),
    "Reclamo": (8, 15),
    "Soporte técnico": (10, 18)
}

# Probabilidad de error del chatbot
INTENT_ERROR_PROBABILITY = {
    "Consultar precios": 0.03,
    "Solicitar información": 0.05,
    "Agendar servicio": 0.07,
    "Cancelar servicio": 0.08,
    "Seguimiento": 0.10,
    "Reclamo": 0.25,
    "Soporte técnico": 0.30
}


# ======================================================
# SERVICIOS
# ======================================================

SERVICES = [
    "Atención Comercial",
    "Ventas",
    "Soporte",
    "Postventa",
    "Atención al Cliente"
]


# ======================================================
# TIPOS DE CLIENTES
# ======================================================

CUSTOMER_TYPES = [
    "Nuevo",
    "Frecuente",
    "VIP"
]

CUSTOMER_TYPE_WEIGHTS = [
    0.55,
    0.35,
    0.10
]

BASE_CONVERSION_PROBABILITY = {
    "Nuevo": 0.25,
    "Frecuente": 0.55,
    "VIP": 0.80
}

# ======================================================
# DISTRITOS
# ======================================================

DISTRICTS = [
    "Miraflores",
    "San Isidro",
    "Surco",
    "La Molina",
    "San Borja",
    "Barranco",
    "Lince",
    "Pueblo Libre",
    "Jesús María",
    "San Miguel"
]


# ======================================================
# GÉNEROS
# ======================================================

GENDERS = [
    "Masculino",
    "Femenino"
]


# ======================================================
# ESTADOS DE LA CONVERSACIÓN
# ======================================================

STATUS = [
    "Finalizada",
    "Abandonada"
]

STATUS_WEIGHTS = [
    0.82,
    0.18
]

CHANNEL_CONVERSION_MODIFIER = {
    "WhatsApp": 0.10,
    "Web": 0.05,
    "Facebook": -0.05,
    "Instagram": -0.10,
    "Telegram": -0.15
}


# ======================================================
# SATISFACCIÓN DEL CLIENTE
# ======================================================

SATISFACTION_VALUES = [
    1,
    2,
    3,
    4,
    5
]


# ======================================================
# CONFIGURACIÓN DEL PROYECTO
# ======================================================

# Cantidad de conversaciones a generar
TOTAL_CONVERSATIONS = 10000

# Año de simulación
SIMULATION_YEAR = 2025

# País de Faker
FAKER_LOCALE = "es_ES"