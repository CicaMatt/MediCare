from flaskDir import test
class Farmaco(test.Model):
    ID = test.Column(test.Integer, primary_key=True, autoincrement=True)
    prezzo = test.Column(test.Float, nullable=False)
    nome = test.Column(test.String(255), nullable=False)
    categoria = test.Column(test.String(100), nullable=False)
    descrizione = test.Column(test.Text, nullable=False)
    immagine = test.Column(test.String(255), nullable=False)
    __table_args__ = (test.UniqueConstraint('nome', 'categoria'),)

