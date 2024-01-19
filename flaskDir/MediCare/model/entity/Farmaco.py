from flaskDir import db
class Farmaco(db.Model):
    """
    La classe Farmaco rappresenta il modello di dati per la tabella "farmaco" nel database.

    Attributi:
    - ID (int): Identificatore univoco del farmaco, chiave primaria (autoincrement).
    - prezzo (float): Prezzo del farmaco.
    - nome (str): Nome del farmaco.
    - categoria (str): Categoria a cui appartiene il farmaco.
    - descrizione (str): Descrizione del farmaco.
    - immagine (str): Percorso dell'immagine del farmaco.

    Vincoli:
    - UniqueConstraint('nome', 'categoria'): Vincolo univoco su combinazione di nome e categoria.

    """
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prezzo = db.Column(db.Float, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descrizione = db.Column(db.Text, nullable=False)
    immagine = db.Column(db.String(255), nullable=False)
    __table_args__ = (db.UniqueConstraint('nome', 'categoria'),)

