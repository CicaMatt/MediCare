from flaskDir import db

class VisualizzaFarmaco(db.Model):
    Farmaco = db.Column(db.Integer, db.ForeignKey('farmaco.ID'), primary_key=True)
    Paziente = db.Column(db.String(16), db.ForeignKey('paziente.CF'), primary_key=True)