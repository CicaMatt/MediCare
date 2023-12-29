-- Creazione del database
CREATE DATABASE IF NOT EXISTS Medicare;

-- Utilizzo del database appena creato
USE Medicare;



-- Creazione della tabella EnteSanitario
CREATE TABLE IF NOT EXISTS EnteSanitario (
    nome VARCHAR(255) not null,
    email VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) not null
);

-- Creazione della tabella Medico
CREATE TABLE IF NOT EXISTS Medico (
    email VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) not null,
    nome VARCHAR(255),
    cognome VARCHAR(255),
    reparto VARCHAR(255),
    enteSanitario VARCHAR(255) not null,
    iscrizioneAlbo INT,
    specializzazione VARCHAR(255) not null,
    FOREIGN KEY (enteSanitario) REFERENCES EnteSanitario(email)
     on update cascade
	 on delete no action
);

-- Creazione della tabella Farmaco
CREATE TABLE IF NOT EXISTS Farmaco (
    ID INT auto_increment Primary Key,
    prezzo FLOAT not null,
    nome VARCHAR(255) not null,
    categoria varchar(100) not null,
    descrizione text not null,
    UNIQUE(nome, categoria)
);

-- Creazione della tabella Paziente
CREATE TABLE IF NOT EXISTS Paziente (
    CF VARCHAR(16) PRIMARY KEY,
    chiaveSPID INT not null,
    nome VARCHAR(255) not null,
    cognome VARCHAR(255) not null,
    email VARCHAR(255) not null,
    password VARCHAR(255) not null,
    cellulare VARCHAR(10) not null,
    domicilio VARCHAR(255) not null,
    dataNascita DATE not null,
    luogoNascita VARCHAR(255) not null,
    sesso Varchar(30) not null
);

-- Creazione della tabella MetodoPagamento
CREATE TABLE IF NOT EXISTS MetodoPagamento (
    CVV INT not null,
    PAN VARCHAR(16) not null,
    nometitolare VARCHAR(255) not null,
    dataScadenza DATE not null,
    beneficiario VARCHAR(16) not null,
    PRIMARY KEY(PAN,beneficiario),
    FOREIGN KEY (beneficiario) REFERENCES Paziente(CF)
    on update cascade
    on delete no action
);

-- Creazione della tabella DocumentoSanitario
CREATE TABLE IF NOT EXISTS DocumentoSanitario (
    NumeroDocumento VARCHAR(20) not null,
    tipo VARCHAR(255) not null,
    dataEmissione DATE not null,
    descrizione TEXT not null,
    titolare VARCHAR(16),
    PRIMARY KEY(NumeroDocumento, titolare),
    FOREIGN KEY (titolare) REFERENCES Paziente(CF)
     on update cascade
     on delete no action
);
-- Creazione della tabella Prenotazione
CREATE TABLE IF NOT EXISTS Prenotazione (
    ID INT auto_increment,
    oraVisita INT not null,
    dataVisita DATE not null,
    tipoVisita VARCHAR(255) not null,
    pazienteCF VARCHAR(16),
    medico VARCHAR(255),
    FOREIGN KEY (pazienteCF) REFERENCES Paziente(CF)
     on update cascade
     on delete no action,
    FOREIGN KEY (medico) REFERENCES Medico(email)
     on update cascade
     on delete no action,
    PRIMARY KEY(ID,pazienteCF,medico)
);

CREATE TABLE IF NOT EXISTS VisualizzaFarmaco(
Farmaco int auto_increment not null,
Paziente VARCHAR(16) not null,
PRIMARY KEY(Farmaco, Paziente),
FOREIGN KEY(Farmaco) REFERENCES Farmaco(ID)
 on update cascade
 on delete no action,
FOREIGN KEY (Paziente) REFERENCES Paziente(CF)
 on update cascade
 on delete no action
);

CREATE TABLE IF NOT EXISTS ConsultaFarmaco(
Farmaco int auto_increment not null,
Medico VARCHAR(255) not null,
PRIMARY KEY(Farmaco,Medico),
FOREIGN KEY(Farmaco) REFERENCES Farmaco(ID)
 on update cascade
 on delete no action,
FOREIGN KEY(Medico) REFERENCES Medico(email)
 on update cascade
 on delete no action
);

CREATE TABLE IF NOT EXISTS ConsultaFascicolo(
Medico VARCHAR(255) not null,
Documento VARCHAR(20) not null,
PRIMARY KEY(Medico, Documento),
FOREIGN KEY(Medico) REFERENCES Medico(email)
 on update cascade
 on delete no action,
FOREIGN KEY(Documento) REFERENCES DocumentoSanitario(NumeroDocumento)
 on update cascade
 on delete no action
);