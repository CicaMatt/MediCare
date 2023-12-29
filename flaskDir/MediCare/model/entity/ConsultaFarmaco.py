from flaskDir import db

class ConsultaFarmaco(db.Model):
    Farmaco = db.Column(db.Integer, db.ForeignKey('farmaco.ID'), primary_key=True)
    Medico = db.Column(db.String(255), db.ForeignKey('medico.email'), primary_key=True)