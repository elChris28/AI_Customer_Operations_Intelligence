"""
====================================================
AI Customer Operations Intelligence
----------------------------------------------------
Aplicación principal del proyecto.

Tecnologías:
- SQL Server
- Python
- Streamlit
- Business Intelligence

Autor:  Christofer Ynga
====================================================
"""

import streamlit as st

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
    conversaciones_por_intencion,
    obtener_conversaciones
)

from utils import (
    responder_pregunta,
    preguntas_sugeridas
)

from insights import (
    insight_canal,
    insight_servicio,
    insight_errores,
    insight_estado,
    insight_intenciones,
    insight_kpi
)

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="AI Customer Operations Intelligence",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Customer Operations Intelligence")

st.caption(
    "Centro de Inteligencia Operativa desarrollado con SQL Server, Python y Streamlit."
)

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 KPIs",
        "🤖 Copiloto",
        "📈 Explorador",
        "ℹ️ Acerca"
    ]
)

# =====================================================
# TAB KPIs
# =====================================================

with tab1:

    st.subheader("Indicadores principales")

    total = total_conversaciones()
    conversiones = total_conversiones()
    conversion = tasa_conversion()
    satisfaccion = satisfaccion_promedio()
    tiempo = tiempo_promedio()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Conversaciones",
        f"{total:,}"
    )

    col2.metric(
        "Conversiones",
        f"{conversiones:,}"
    )

    col3.metric(
        "Conversión",
        f"{conversion}%"
    )

    col4.metric(
        "Satisfacción",
        satisfaccion
    )

    col5.metric(
        "Tiempo Promedio",
        f"{tiempo} min"
    )

    st.divider()

    st.subheader("Interpretación automática")

    st.success(insight_kpi("conversion", conversion))

    st.info(insight_kpi("satisfaccion", satisfaccion))

    st.warning(insight_kpi("tiempo", tiempo))

# =====================================================
# TAB COPILOTO
# =====================================================

with tab2:

    st.subheader("Copiloto Analítico")

    st.write(
        "Realiza preguntas relacionadas con el desempeño del chatbot."
    )

    with st.expander("Preguntas sugeridas"):

        for pregunta in preguntas_sugeridas():

            st.write("•", pregunta)

    pregunta = st.text_input(
        "Escribe tu pregunta:"
    )

    if pregunta:

        resultado = responder_pregunta(pregunta)

        if resultado is None:

            st.error(
                "No pude comprender la pregunta."
            )

        else:

            # =====================================================
            # DATAFRAME
            # =====================================================

            if hasattr(resultado, "columns"):

                st.dataframe(
                    resultado,
                    use_container_width=True
                )

                if len(resultado.columns) == 2:

                    st.bar_chart(
                        resultado.set_index(
                            resultado.columns[0]
                        )
                    )

                columnas = resultado.columns

                if "Canal" in columnas:

                    st.success(
                        insight_canal(resultado)
                    )

                elif "Servicio" in columnas:

                    st.success(
                        insight_servicio(resultado)
                    )

                elif "Errores" in columnas:

                    st.warning(
                        insight_errores(resultado)
                    )

                elif "EstadoConversacion" in columnas:

                    st.info(
                        insight_estado(resultado)
                    )

                elif "Intencion" in columnas:

                    st.success(
                        insight_intenciones(resultado)
                    )

            else:

                st.metric(
                    "Resultado",
                    resultado
                )

# =====================================================
# TAB EXPLORADOR
# =====================================================

with tab3:

    st.subheader("Explorador de Conversaciones")
    st.write("Muestra las primeras 100 conversaciones")

    df = obtener_conversaciones()

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Descargar CSV",
        data=csv,
        file_name="conversaciones.csv",
        mime="text/csv"
    )

# =====================================================
# TAB ACERCA
# =====================================================

with tab4:

    st.subheader("Acerca del Proyecto")

    st.markdown("""

## AI Customer Operations Intelligence

Proyecto desarrollado para demostrar competencias en:

- SQL Server
- Python ETL
- Data Warehouse
- Power BI
- Streamlit
- Business Intelligence

### Funcionalidades

- Modelo estrella
- ETL automatizado
- Dashboard Power BI
- Copiloto Analítico
- Explorador de datos
- Generación automática de insights

### Tecnologías

- SQL Server
- Python
- Pandas
- PyODBC
- Streamlit
- Power BI

""")

    st.success(
        "Proyecto desarrollado con fines educativos y como portafolio profesional."
    )