DROP TABLE IF EXISTS donne;

CREATE TABLE donne (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    age int,
    sexe VARCHAR(30),
    tdt VARCHAR(20),
    par int,
    cholesterol int,
    gaj int,
    ecg VARCHAR(30),
    fmax int,
    angine VARCHAR(30),
    depres int,
    pente VARCHAR(30)

);