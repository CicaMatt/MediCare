use medicare;

INSERT INTO ente_sanitario Values("Policlinico Universitario A. Gemelli ","policlinotwin@pec.it","twin2023");
INSERT INTO ente_sanitario Values("Ospedale Papa Giovanni XXIII", "ospedaleBergamo23@pec.it","Papa23");
INSERT INTO farmaco(prezzo,nome,categoria,descrizione) VALUES(2.45,"Tachipirina", "Sciroppo","Il Miglior rimedio per l'influenza, un cucchiaio di Tachipirina e si saluta l'influenza");
INSERT INTO farmaco(prezzo,nome,categoria,descrizione) VALUES(2.60,"Tachipirina","Idrosolubile","Farmaco che non richiede prescrizione, è il miglior metodo per indebolire una forte influenza, per la somministrazione è necessario un bicchiere di acqua in cui scioglierla. Nella confezione sono presenti 20 bustine");
INSERT INTO farmaco(prezzo, nome, categoria, descrizione) VALUES(4.91,"OkiTask","Idrosolubile","Un farmaco molto potente idrosolubile che è consigliato somministrare ad un paziente più maturo. La confezione contiene 20 bustine di OkiTask al sapore di menta");
INSERT INTO farmaco(prezzo,nome, categoria, descrizione) VALUES(8.90,"Moment Act","Compresse","Confezione da 20 compresse somministrabili 1 ogni 12 ore per adulti con età superiore ai 12 anni, farmaco ideale per far scomparire completamente le forti emicrania alla testa");
INSERT INTO farmaco(prezzo, nome, categoria, descrizione) VALUES(4.05,"Brufen","Compresse","Brufen è un antinfiammatorio utile per il trattamento del dolore come mal di testa,mal di denti,dolori mestruali, febbre e dolore associati a raffreddore. Somministrabile a paiente sopra i6 anni di età");
INSERT INTO medico(email,password_hash, nome,cognome,iscrizione_albo,specializzazione,città) VALUES("giovannicasaburi@gmail.com","IlDottorCasaburi","Giovanni","Casaburi",1,"Oculistica","Piccola Svizzera");
INSERT INTO medico(email,password_hash,nome,cognome,iscrizione_albo, specializzazione,città) VALUES("barbaradamico@gmail.com","DelfinoBiricchino","Barbara","D'Amico",22,"Oculistica","Benevento");
INSERT INTO medico(email,password_hash,reparto,ente_sanitario,specializzazione,città) VALUES("repartoOcchiGemelli@gmail.com","OcchiGemelli","oculisticaGemelli","policlinotwin@pec.it","Oculistica","Roma");
INSERT INTO medico(email, password_hash,nome,cognome, iscrizione_albo,specializzazione,città) VALUES("luigipagano@hgmail.com","HeartPagano","Luigi","Pagano",15,"Cardiologia","Cava de'Tirreni");
INSERT INTO medico(email, password_hash, nome, cognome, iscrizione_albo, specializzazione,città) VALUES("paolochecchi20@gmail.com","PurpleDoc","Paolo","Cecchi",12,"Cardiologia","Firenze");
INSERT INTO medico(email, password_hash,reparto, ente_sanitario, specializzazione, città) VALUES("repartoCardio44@gmail.com","SaveTheHeart","CardiologiaXXIII","ospedaleBergamo23@pec.it","Cardiologia","Bergamo");
INSERT INTO medico(email, password_hash, nome, cognome, iscrizione_albo, specializzazione, città) VALUES("angelaromano10@gmail.com","TakeCareB","Angela","Romano",24,"Ginecologia","Roma");
INSERT INTO medico(email, password_hash, reparto, ente_sanitario, specializzazione, città) VALUES("repartoGinecologiGemelli@gmail.com","Twins","Ginecologi","policlinotwin@pec.it","Ginecologia", "Roma");
INSERT INTO medico(email, password_hash, reparto, ente_sanitario, specializzazione, città) VALUES("repartoUrologiaGemelli@gmail.com","UroTwin","reparto Urologi","policlinotwin@pec.it","Urologia","Roma");
INSERT INTO medico(email, password_hash, nome, cognome, iscrizione_albo, specializzazione, città) VALUES("gianmarcotocco@gmail.com","ToccoUro","Gianmarco","Tocco",54,"Urologia","Napoli");
INSERT INTO medico(email, password_hash, reparto, ente_sanitario, specializzazione, città) VALUES ("repartoEmatologiGemelli@gmail.com","Rome's Blood","reparto Ematologi","policlinotwin@pec.it","Ematologia","Roma")
