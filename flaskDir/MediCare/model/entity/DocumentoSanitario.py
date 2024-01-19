from flaskDir import db

class DocumentoSanitario(db.Model):
    """
    La classe DocumentoSanitario rappresenta il modello di dati per la tabella "documento_sanitario" nel database.

    Attributi:
    - NumeroDocumento (str): Campo che rappresenta il numero del documento sanitario. È una chiave primaria.
    - tipo (str): Campo che rappresenta il tipo di documento sanitario.
    - dataEmissione (Date): Campo che rappresenta la data di emissione del documento sanitario.
    - descrizione (str): Campo che rappresenta la descrizione del documento sanitario.
    - richiamo (Date, opzionale): Campo che rappresenta la data di richiamo associata al documento sanitario (opzionale).
    - titolare (str): Campo che rappresenta il codice fiscale del paziente a cui il documento sanitario è associato.
      È una chiave esterna che fa riferimento alla colonna 'CF' nella tabella 'paziente'. È anche parte delle chiavi primarie
      composite insieme a 'NumeroDocumento'.

    """
    NumeroDocumento = db.Column(db.String(20), nullable=False, primary_key=True)
    tipo = db.Column(db.String(255), nullable=False)
    dataEmissione = db.Column(db.Date, nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    richiamo= db.Column(db.Date, nullable=True)
    titolare = db.Column(db.String(16), db.ForeignKey('paziente.CF'), nullable=True, primary_key=True)

