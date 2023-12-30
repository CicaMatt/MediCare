from flaskDir import db

class EnteSanitario(db.Model):
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    reparti = db.relationship("EnteSanitario", backref="reparti", lazy=True)