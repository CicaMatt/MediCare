import re

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir.MediCare.model.entity.EnteSanitario import EnteSanitario, Medico
from flaskDir import db, app
class EnteService:
    @staticmethod
    def retrieveEnte(email, password):
        """
        Recupera un ente sanitario dal database in base all'indirizzo email e alla password.

        Args:
            email (str): L'indirizzo email dell'ente sanitario.
            password (str): La password dell'ente sanitario.

        Returns:
            EnteSanitario or None: L'oggetto EnteSanitario corrispondente all'indirizzo email e alla password forniti, o None se non trovato.
        """
        ente = db.session.scalar(sqlalchemy.select(EnteSanitario).where(EnteSanitario.email == email))
        if ente is None or not ente.check_password(password):
            return None
        return ente

    @staticmethod
    def creaReparto(nome,email,password,specializzazione,citta,ente):
        """
        Crea un nuovo reparto medico associato a un ente sanitario nel sistema.

        Args:
            nome (str): Il nome del reparto medico.
            email (str): L'indirizzo email del medico responsabile del reparto.
            password (str): La password del medico responsabile del reparto.
            specializzazione (str): La specializzazione del medico responsabile del reparto.
            citta (str): La città in cui si trova il reparto medico.
            ente (str): L'email dell'Ente sanitario associato al reparto.

        Returns:
            bool: True se la creazione del reparto ha avuto successo, False altrimenti.
        """
        formato_email=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not formato_email.match(email):return False
        if not 8<=len(password)<=20:return False
        with app.app_context():
            try:
                medico=Medico()
                medico.reparto=nome
                medico.email=email
                medico.set_password(password)
                medico.specializzazione=specializzazione
                medico.città=citta
                medico.tariffa=20.00
                medico.ente_sanitario=ente

                db.session.add(medico)
                db.session.commit()
                return True
            except SQLAlchemyError as e:
                return False


    @staticmethod
    def deleteReparto(email):
        """
        Elimina un reparto medico dal sistema in base all'indirizzo email del medico responsabile.

        Args:
            email (str): L'indirizzo email del medico responsabile del reparto.

        Returns:
            None
        """
        with app.app_context():
            medico=db.session.scalar(sqlalchemy.select(Medico).where(Medico.email ==email))
            db.session.delete(medico)
            db.session.commit()
