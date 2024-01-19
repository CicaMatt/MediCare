from flaskDir import db

class ConsultaFascicolo(db.Model):
    """
    La classe ConsultaFascicolo rappresenta il modello di dati per la tabella "consulta_fascicolo" nel database.

    Attributi:
    - Medico (str): Campo che rappresenta l'email del medico che ha consultato un documento nel fascicolo. È una chiave esterna
      che fa riferimento alla colonna 'email' nella tabella 'medico'.
    - Documento (str): Campo che rappresenta il numero del documento sanitario consultato. È una chiave esterna che fa riferimento
      alla colonna 'NumeroDocumento' nella tabella 'documento_sanitario'.

    Entrambi questi campi vengono utilizzati come chiavi primarie composite, il che significa che la combinazione unica di
    `Medico` e `Documento` identifica in modo univoco una riga nella tabella `ConsultaFascicolo`.

    """
    Medico = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)
    Documento = db.Column(db.String(20), db.ForeignKey('documento_sanitario.NumeroDocumento'), primary_key=True)

