import functools

import bcrypt
from flask import session, redirect, url_for

from flaskDir import db
from flask_login import UserMixin


def paziente_required(func):
    """
    Decoratore per verificare se l'utente in sessione è un paziente.

    Args:
    - func (function): La funzione da decorare.

    Returns:
    - function: La funzione decorata.

    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_role') == 'paziente':
            return func(*args, **kwargs)
        return redirect(url_for('home'))

    return wrapper


class Paziente(db.Model, UserMixin):
    """
    Classe che rappresenta un paziente.

    Attributi:
    - CF (str): Codice Fiscale del paziente (chiave primaria).
    - chiaveSPID (int): Chiave SPID associata al paziente.
    - nome (str): Nome del paziente.
    - cognome (str): Cognome del paziente.
    - email (str): Indirizzo email del paziente.
    - password_hash (str): Hash della password del paziente.
    - cellulare (str): Numero di cellulare del paziente.
    - domicilio (str): Indirizzo di domicilio del paziente.
    - dataNascita (Date): Data di nascita del paziente.
    - luogoNascita (str): Luogo di nascita del paziente.
    - sesso (str): Genere del paziente.
    - ISEE_ordinario (Numeric): Valore dell'ISEE ordinario del paziente.
    - carte (list): Lista di carte di pagamento associate al paziente.

    Metodi:
    - set_password(password): Imposta la password del paziente.
    - check_password(password): Verifica se la password fornita è corretta.
    - get_id(): Restituisce il Codice Fiscale del paziente come identificatore unico.

    """
    CF = db.Column(db.String(16), primary_key=True)
    chiaveSPID = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    cognome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    cellulare = db.Column(db.String(10), nullable=False)
    domicilio = db.Column(db.String(255), nullable=False)
    dataNascita = db.Column(db.Date, nullable=False)
    luogoNascita = db.Column(db.String(255), nullable=False)
    sesso = db.Column(db.String(30), nullable=False)
    ISEE_ordinario = db.Column(db.Numeric(precision=9, scale=2),
                               nullable=True)  # cambiare salvataggio di un paziente nei services
    carte = db.relationship("MetodoPagamento", backref="paziente", lazy=True)

    def set_password(self, password):
        """
        Imposta la password del paziente.

        Args:
        - password (str): La password da impostare.

        Returns:
        - None

        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password_hash = hashed

    def check_password(self, password):
        """
        Verifica se la password fornita è corretta.

        Args:
        - password (str): La password da verificare.

        Returns:
        - bool: True se la password è corretta, False altrimenti.

        """
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def get_id(self):
        """
        Restituisce il Codice Fiscale del paziente come identificatore unico.

        Args:
        - None

        Returns:
        - str: Il Codice Fiscale del paziente.

        """
        return self.CF
