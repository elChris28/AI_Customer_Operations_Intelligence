"""
====================================================
insights.py
----------------------------------------------------
Generador de insights y recomendaciones de negocio.

Responsabilidad:
- Interpretar resultados de consultas.
- Generar recomendaciones automáticas.
- Mantener separada la lógica de negocio de la interfaz.
====================================================
"""

import pandas as pd


# ====================================================
# CANAL
# ====================================================

def insight_canal(df: pd.DataFrame):

    canal = df.iloc[0]["Canal"]
    conversiones = int(df.iloc[0]["Conversiones"])

    return f"""
### 📌 Insight

El canal con mayor conversión es **{canal}**, con **{conversiones} conversiones**.

### 💡 Recomendación

- Priorizar campañas en este canal.
- Analizar qué factores impulsan su desempeño.
- Replicar esas estrategias en los canales con menor conversión.
"""


# ====================================================
# SERVICIO
# ====================================================

def insight_servicio(df: pd.DataFrame):

    servicio = df.iloc[0]["Servicio"]
    promedio = round(float(df.iloc[0]["Satisfaccion"]), 2)

    return f"""
### 📌 Insight

El servicio con mayor satisfacción es **{servicio}** con una calificación promedio de **{promedio}/5**.

### 💡 Recomendación

- Analizar por qué este servicio obtiene mejores valoraciones.
- Replicar buenas prácticas en otros servicios.
- Monitorear periódicamente la satisfacción del cliente.
"""


# ====================================================
# ERRORES
# ====================================================

def insight_errores(df: pd.DataFrame):

    intencion = df.iloc[0]["Intencion"]
    errores = int(df.iloc[0]["Errores"])

    return f"""
### 📌 Insight

La intención **{intencion}** concentra la mayor cantidad de errores (**{errores}**).

### 💡 Recomendación

- Revisar el flujo conversacional asociado.
- Mejorar las respuestas automáticas.
- Evaluar si faltan ejemplos de entrenamiento para esta intención.
"""


# ====================================================
# ESTADOS
# ====================================================

def insight_estado(df: pd.DataFrame):

    estado = df.iloc[0]["EstadoConversacion"]
    total = int(df.iloc[0]["Total"])

    return f"""
### 📌 Insight

El estado predominante es **{estado}**, con **{total} conversaciones**.

### 💡 Recomendación

- Analizar la distribución de estados para identificar posibles cuellos de botella.
- Revisar especialmente los estados relacionados con abandono o error.
"""


# ====================================================
# INTENCIONES
# ====================================================

def insight_intenciones(df: pd.DataFrame):

    intencion = df.iloc[0]["Intencion"]
    total = int(df.iloc[0]["Total"])

    return f"""
### 📌 Insight

La intención más frecuente es **{intencion}**, con **{total} conversaciones**.

### 💡 Recomendación

- Optimizar los flujos relacionados con esta intención.
- Crear respuestas más completas para reducir tiempos de atención.
- Priorizar mejoras donde existe mayor volumen de consultas.
"""


# ====================================================
# KPIs
# ====================================================

def insight_kpi(nombre, valor):

    if nombre == "conversion":

        if valor >= 70:
            return "🟢 Excelente tasa de conversión."

        elif valor >= 50:
            return "🟡 Conversión aceptable, aunque puede optimizarse."

        else:
            return "🔴 Conversión baja. Se recomienda revisar el proceso de atención."

    if nombre == "satisfaccion":

        if valor >= 4.5:
            return "🟢 Nivel de satisfacción muy alto."

        elif valor >= 4:
            return "🟡 Satisfacción adecuada."

        else:
            return "🔴 La satisfacción es baja y requiere atención."

    if nombre == "tiempo":

        if valor <= 5:
            return "🟢 Tiempo de atención eficiente."

        elif valor <= 10:
            return "🟡 Tiempo de atención aceptable."

        else:
            return "🔴 El tiempo promedio es elevado. Conviene revisar el proceso."

    return ""