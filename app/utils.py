"""
====================================================
utils.py
----------------------------------------------------
Motor de clasificación de preguntas.

Responsabilidad:
- Interpretar la pregunta del usuario.
- Detectar la intención.
- Ejecutar la consulta correspondiente.
- Devolver el resultado.
====================================================
"""

import unicodedata

from queries import (
    total_conversaciones,
    total_conversiones,
    tasa_conversion,
    satisfaccion_promedio,
    tiempo_promedio,
    conversion_por_canal,
    errores_por_intencion,
    satisfaccion_por_servicio,
    conversaciones_por_estado,
    conversaciones_por_canal,
    conversaciones_por_intencion
)


# ====================================================
# NORMALIZAR TEXTO
# ====================================================

def normalizar_texto(texto: str) -> str:
    """
    Convierte el texto a minúsculas y elimina tildes.
    """
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )

    return texto

# ====================================================
# DICCIONARIO DE INTENCIONES
# ====================================================

CONSULTAS = {

    "total_conversaciones": {
        "keywords": [
            "conversaciones",
            "total conversaciones",
            "cantidad conversaciones",
            "numero conversaciones",
            "cuantas conversaciones"
        ],
        "funcion": total_conversaciones
    },

    "total_conversiones": {
        "keywords": [
            "conversiones",
            "total conversiones"
        ],
        "funcion": total_conversiones
    },

    "tasa_conversion": {
        "keywords": [
            "tasa conversion",
            "porcentaje conversion",
            "conversion"
        ],
        "funcion": tasa_conversion
    },

    "satisfaccion": {
        "keywords": [
            "satisfaccion",
            "promedio satisfaccion",
            "calificacion"
        ],
        "funcion": satisfaccion_promedio
    },

    "tiempo": {
        "keywords": [
            "tiempo",
            "duracion",
            "promedio tiempo"
        ],
        "funcion": tiempo_promedio
    },

    "canal": {
        "keywords": [
            "mejor canal por conversion",
            "canal conversion"
        ],
        "funcion": conversion_por_canal
    },

    "errores": {
        "keywords": [
            "errores",
            "errores intencion",
            "intencion errores"
        ],
        "funcion": errores_por_intencion
    },

    "servicio": {

        "keywords": [
            "servicio",
            "mejor servicio",
            "mayor satisfaccion"
        ],
        "funcion": satisfaccion_por_servicio
    },

    "estado": {
        "keywords": [
            "estado",
            "estado conversaciones"
        ],
        "funcion": conversaciones_por_estado
    },
    "canal": {
        "keywords": [
            "canal con mas conversaciones",
            "canal conversaciones"
        ],
        "funcion": conversaciones_por_canal
    },

    "intencion": {
        "keywords": [
            "intenciones",
            "intencion"
        ],
        "funcion": conversaciones_por_intencion
    }

}


# ====================================================
# RESPONDER PREGUNTA
# ====================================================

def responder_pregunta(pregunta: str):

    pregunta = normalizar_texto(pregunta)
    for consulta in CONSULTAS.values():
        for keyword in consulta["keywords"]:
            if keyword in pregunta:
                return consulta["funcion"]()
            
    return None


# ====================================================
# PREGUNTAS DISPONIBLES
# ====================================================

def preguntas_sugeridas():

    return [
        "¿Cuántas conversaciones hubo?",
        "¿Cuál es la tasa de conversión?",
        "¿Qué canal tiene mayor conversión?",
        "¿Qué intención presenta más errores?",
        "¿Cuál es el servicio con mayor satisfacción?",
        "¿Cuál es el tiempo promedio de atención?",

        "Muéstrame las conversaciones por estado."
    ]