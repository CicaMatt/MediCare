from flaskDir import db, login
from flask_login import UserMixin


@login.user_loader
def load_user(id): #Bisogna aggiungere anche l'utente
    return db.session.get(EnteSanitario, id)

class EnteSanitario(db.Model, UserMixin):
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    reparti = db.relationship("Medico", backref="reparti", lazy=True)



    def getEnteSanitario(self):
        return self.email