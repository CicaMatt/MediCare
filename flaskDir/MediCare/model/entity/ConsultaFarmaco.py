from flaskDir import db


class ConsultaFarmaco(db.Model):
    """
    La classe ConsultaFarmaco rappresenta il modello di dati per la tabella "consulta_farmaco" nel database.

    Attributi: - Farmaco (int): Campo che rappresenta l'ID del farmaco consultato. È una chiave esterna che fa
    riferimento alla colonna 'ID' nella tabella 'farmaco'. - Medico (str): Campo che rappresenta l'email del medico
    che ha consultato un farmaco. È una chiave esterna che fa riferimento alla colonna 'email' nella tabella 'medico'.

    Entrambi questi campi vengono utilizzati come chiavi primarie composite, il che significa che la combinazione
    unica di `Farmaco` e `Medico` identifica in modo univoco una riga nella tabella `ConsultaFarmaco`.

    """
    Farmaco = db.Column(db.Integer, db.ForeignKey('farmaco.ID'), primary_key=True)
    Medico = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)
