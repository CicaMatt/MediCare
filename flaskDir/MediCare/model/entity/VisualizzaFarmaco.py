from flaskDir import db


class VisualizzaFarmaco(db.Model):
    """
    Classe che rappresenta l'associazione tra un farmaco e un paziente per la visualizzazione.

    Attributi:
    - Farmaco (int): Identificatore unico del farmaco (chiave primaria, chiave esterna verso Farmaco).
    - Paziente (str): Codice Fiscale del paziente (chiave primaria, chiave esterna verso Paziente).

    """
    Farmaco = db.Column(db.Integer, db.ForeignKey('farmaco.ID'), primary_key=True)
    Paziente = db.Column(db.String(16), db.ForeignKey('paziente.CF'), primary_key=True)
