"""
====================================================
queries.py
----------------------------------------------------
Consultas SQL del proyecto AI Customer Operations BI.

Responsabilidad:
- Ejecutar consultas sobre el Data Warehouse.
- Devolver resultados como DataFrames o valores simples.
- No contiene lógica de interfaz ni reglas de negocio.
====================================================
"""

import pandas as pd
from database import get_connection


# ====================================================
# FUNCIÓN BASE
# ====================================================

def ejecutar_consulta(query: str) -> pd.DataFrame:
    """
    Ejecuta una consulta SQL y devuelve un DataFrame.
    """

    connection = get_connection()

    try:
        df = pd.read_sql(query, connection)
        return df

    finally:
        connection.close()


# ====================================================
# KPIs
# ====================================================

def total_conversaciones():

    query = """
    SELECT COUNT(*) AS Total
    FROM FactConversaciones
    """

    df = ejecutar_consulta(query)

    return int(df.iloc[0]["Total"])


def total_conversiones():

    query = """
    SELECT COUNT(*) AS Total
    FROM FactConversaciones
    WHERE Convertido = 1
    """

    df = ejecutar_consulta(query)

    return int(df.iloc[0]["Total"])


def tasa_conversion():

    query = """
    SELECT
        CAST(
            100.0 *
            SUM(CASE WHEN Convertido = 1 THEN 1 ELSE 0 END)
            /
            COUNT(*)
        AS DECIMAL(5,2))
        AS Conversion
    FROM FactConversaciones
    """

    df = ejecutar_consulta(query)

    return float(df.iloc[0]["Conversion"])


def satisfaccion_promedio():

    query = """
    SELECT
        AVG(CAST(Satisfaccion AS FLOAT))
        AS Promedio
    FROM FactConversaciones
    """

    df = ejecutar_consulta(query)

    return round(float(df.iloc[0]["Promedio"]), 2)


def tiempo_promedio():

    query = """
    SELECT
        AVG(CAST(DuracionMinutos AS FLOAT))
        AS Promedio
    FROM FactConversaciones
    """

    df = ejecutar_consulta(query)

    return round(float(df.iloc[0]["Promedio"]), 2)


# ====================================================
# CONSULTAS ANALÍTICAS
# ====================================================

def conversion_por_canal():

    query = """
    SELECT
        c.Canal,
        COUNT(*) AS Conversiones
    FROM FactConversaciones f

    INNER JOIN DimCanal c
    ON c.CanalID = f.CanalID

    WHERE Convertido = 1
    GROUP BY c.Canal
    ORDER BY Conversiones DESC
    """
    return ejecutar_consulta(query)


def errores_por_intencion():

    query = """
    SELECT
        i.Intencion,
        COUNT(*) AS Errores
    FROM FactConversaciones f

    INNER JOIN DimIntencion i
    ON i.IntencionID = f.IntencionID

    WHERE TuvoError = 1
    GROUP BY i.Intencion
    ORDER BY Errores DESC
    """
    return ejecutar_consulta(query)


def satisfaccion_por_servicio():

    query = """
    SELECT
        s.Servicio,
        AVG(CAST(Satisfaccion AS FLOAT)) AS Satisfaccion
    FROM FactConversaciones f

    INNER JOIN DimServicio s
    ON s.ServicioID = f.ServicioID

    GROUP BY s.Servicio
    ORDER BY Satisfaccion DESC
    """
    return ejecutar_consulta(query)


def conversaciones_por_estado():

    query = """
    SELECT
        EstadoConversacion,
        COUNT(*) AS Total
    FROM FactConversaciones

    GROUP BY EstadoConversacion
    ORDER BY Total DESC
    """
    return ejecutar_consulta(query)


def conversaciones_por_canal():

    query = """
    SELECT
        c.Canal,
        COUNT(*) AS Total
    FROM FactConversaciones f

    INNER JOIN DimCanal c
    ON c.CanalID = f.CanalID

    GROUP BY c.Canal
    ORDER BY Total DESC
    """

    return ejecutar_consulta(query)


def conversaciones_por_intencion():

    query = """
    SELECT
        i.Intencion,
        COUNT(*) AS Total
    FROM FactConversaciones f

    INNER JOIN DimIntencion i
    ON i.IntencionID = f.IntencionID

    GROUP BY i.Intencion
    ORDER BY Total DESC
    """
    return ejecutar_consulta(query)


# ====================================================
# EXPLORADOR
# ====================================================

def obtener_conversaciones():

    query = """
    SELECT TOP (100)
        f.ConversationID,
        c.Canal,
        i.Intencion,
        s.Servicio,
        f.EstadoConversacion,
        f.Convertido,
        f.Satisfaccion,
        f.DuracionMinutos
    FROM FactConversaciones f

    INNER JOIN DimCanal c
    ON c.CanalID = f.CanalID

    INNER JOIN DimIntencion i
    ON i.IntencionID = f.IntencionID

    INNER JOIN DimServicio s
    ON s.ServicioID = f.ServicioID
    """
    return ejecutar_consulta(query)