from functools import wraps

import bcrypt
from flask import session, redirect, url_for
from flask_login import UserMixin

from flaskDir import db


def ente_required(func):
    """
    Decoratore per richiedere l'autenticazione come ente sanitario.

    Args:
    - func (callable): Funzione da decorare.

    Returns:
    - callable: Funzione decorata.

    """

    @wraps
    def wrapper(*args, **kwargs):
        if session.get('user_role') == 'ente':
            return func(*args, **kwargs)
        return redirect(url_for('home'))

    return wrapper


class EnteSanitario(db.Model, UserMixin):
    """
    La classe EnteSanitario rappresenta il modello di dati per la tabella "ente_sanitario" nel database.

    Attributi:
    - nome (str): Nome dell'ente sanitario.
    - email (str): Indirizzo email dell'ente sanitario, che funge anche da chiave primaria.
    - password_hash (str): Hash della password dell'ente sanitario.
    - città (str): Città in cui si trova l'ente sanitario.
    - reparti (relationship): Relazione con la tabella "medico" tramite la colonna "reparti".

    Metodi:
    - get_id(): Restituisce l'ID dell'ente sanitario, che corrisponde all'indirizzo email.
    - set_password(password): Setta la password dell'ente sanitario.
    - check_password(password): Verifica se una password fornita è corretta.

    """
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True)
    password_hash = db.Column(db.String(255), nullable=False)
    # noinspection NonAsciiCharacters
    città = db.Column(db.String(255), nullable=False)
    reparti = db.relationship("Medico", backref="reparti", lazy=True)

    def get_id(self):
        """
        Restituisce l'ID dell'ente sanitario, che corrisponde all'indirizzo email.

        Returns:
        - str: Indirizzo email dell'ente sanitario.

        """
        return self.email

    def set_password(self, password):
        """
        Imposta la password dell'ente sanitario.

        Args:
        - password (str): Nuova password.

        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password_hash = hashed

    def check_password(self, password):
        """
        Verifica se una password fornita è corretta.

        Args:
        - password (str): Password da verificare.

        Returns:
        - bool: True se la password è corretta, False altrimenti.

        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
