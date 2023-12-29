from flaskDir import db
class Farmaco(db.Model):
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prezzo = db.Column(db.Float, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    __table_args__ = (db.UniqueConstraint('nome', 'categoria'),)

