USE AI_Customer_Operations_Intelligence;
GO

/*=====================================================
ELIMINAR TABLAS SI EXISTEN
=====================================================*/

IF OBJECT_ID('FactConversaciones','U') IS NOT NULL DROP TABLE FactConversaciones;
IF OBJECT_ID('DimCliente','U') IS NOT NULL DROP TABLE DimCliente;
IF OBJECT_ID('DimFecha','U') IS NOT NULL DROP TABLE DimFecha;
IF OBJECT_ID('DimCanal','U') IS NOT NULL DROP TABLE DimCanal;
IF OBJECT_ID('DimServicio','U') IS NOT NULL DROP TABLE DimServicio;
IF OBJECT_ID('DimIntencion','U') IS NOT NULL DROP TABLE DimIntencion;
GO


/*=====================================================
DIM CLIENTE
=====================================================*/

CREATE TABLE DimCliente(
    ClienteID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Edad INT,
	Genero VARCHAR(20),
    Distrito VARCHAR(100),
    TipoCliente VARCHAR(50)
);
GO

/*=====================================================
DIM FECHA
=====================================================*/

CREATE TABLE DimFecha(
    FechaID INT PRIMARY KEY,
    Fecha DATE,
    Anio INT,
    Mes INT,
    NombreMes VARCHAR(20),
    Trimestre INT,
    Dia INT,
    DiaSemana VARCHAR(20),
    Semana INT
);
GO

/*=====================================================
DIM CANAL
=====================================================*/

CREATE TABLE DimCanal(
    CanalID INT PRIMARY KEY,
    Canal VARCHAR(50)
);
GO

/*=====================================================
DIM SERVICIO
=====================================================*/

CREATE TABLE DimServicio(
    ServicioID INT PRIMARY KEY,
    Servicio VARCHAR(100)
);
GO


/*=====================================================
DIM INTENCION
=====================================================*/

CREATE TABLE DimIntencion(
    IntencionID INT PRIMARY KEY,
    Intencion VARCHAR(100)
);
GO

/*=====================================================
FACT CONVERSACIONES
=====================================================*/

CREATE TABLE FactConversaciones(
    ConversationID INT PRIMARY KEY,
    ClienteID INT,
    FechaID INT,
    CanalID INT,
    ServicioID INT,
    IntencionID INT,
    DuracionMinutos INT,
    TuvoError BIT,
    EstadoConversacion VARCHAR(50),
    Convertido BIT,
    Satisfaccion INT,

    CONSTRAINT FK_FactCliente
        FOREIGN KEY (ClienteID)
        REFERENCES DimCliente(ClienteID),

    CONSTRAINT FK_FactFecha
        FOREIGN KEY (FechaID)
        REFERENCES DimFecha(FechaID),

    CONSTRAINT FK_FactCanal
        FOREIGN KEY (CanalID)
        REFERENCES DimCanal(CanalID),

    CONSTRAINT FK_FactServicio
        FOREIGN KEY (ServicioID)
        REFERENCES DimServicio(ServicioID),

    CONSTRAINT FK_FactIntencion
        FOREIGN KEY (IntencionID)
        REFERENCES DimIntencion(IntencionID)
);
GO