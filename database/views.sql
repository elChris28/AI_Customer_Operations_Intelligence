USE AI_Customer_Operations_Intelligence;
GO

--1.Resumen Ejecutivo
CREATE OR ALTER VIEW vw_ResumenEjecutivo
AS
SELECT
COUNT(*) AS TotalConversaciones,
SUM(
    CASE
        WHEN Convertido=1
        THEN 1
        ELSE 0
    END
) AS TotalConversiones,

CAST(100.0 *
SUM(
	CASE
		WHEN Convertido=1
		THEN 1
		ELSE 0
	END
)/COUNT(*)	AS DECIMAL(5,2)
) AS TasaConversion,

AVG(CAST(DuracionMinutos AS FLOAT)) AS TiempoPromedio,
AVG(CAST(Satisfaccion AS FLOAT)) AS SatisfaccionPromedio,

SUM(
	CASE
		WHEN TuvoError=1
		THEN 1
		ELSE 0
	END
) AS ConversacionesConError

FROM FactConversaciones;
GO

--2.EmbudoConversion
CREATE OR ALTER VIEW vw_EmbudoConversion
AS

SELECT
EstadoConversacion,
COUNT(*) AS Total

FROM FactConversaciones

GROUP BY EstadoConversacion;
GO

--3. An�lisis del chatbot
CREATE OR ALTER VIEW vw_AnalisisChatbot
AS

SELECT
i.Intencion,
c.Canal,
COUNT(*) AS Conversaciones,
AVG(CAST(f.Satisfaccion AS FLOAT)) AS Satisfaccion,
AVG(CAST(f.DuracionMinutos AS FLOAT)) AS TiempoPromedio,
SUM(
	CASE
		WHEN f.TuvoError=1
		THEN 1
		ELSE 0
END
) AS Errores

FROM FactConversaciones f

INNER JOIN DimCanal c
ON f.CanalID=c.CanalID

INNER JOIN DimIntencion i
ON f.IntencionID=i.IntencionID

GROUP BY i.Intencion, c.Canal;
GO

--4. Calidad de datos
--Como el reporte esta en CSV, no tiene sentido crear una vista SQL sobre el. 
--En lugar de eso, en Power BI importaremos directamente reports/data_quality_report.csv.