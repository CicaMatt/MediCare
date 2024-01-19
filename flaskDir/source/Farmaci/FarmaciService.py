import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flaskDir import db
from flaskDir.MediCare.model.entity.Farmaco import Farmaco

class FarmaciService:

    @classmethod
    def getFarmaci(cls):
        """
        Restituisce la lista di tutti i farmaci nel catalogo.

        Returns:
            list: Una lista contenente tutti i farmaci nel catalogo.
        """
        return list(db.session.scalars(sqlalchemy.select(Farmaco)))

    @classmethod
    def getDettagliFarmaco(cls, id):
        """
        Restituisce i dettagli di un farmaco dato il suo ID.

        Args:
            id (int): L'ID del farmaco.

        Returns:
            Farmaco: L'oggetto Farmaco con i dettagli.
        """
        return db.session.scalar(sqlalchemy.select(Farmaco).where(Farmaco.ID == id))

    @classmethod
    def getSuggeriti(cls, tipo, id):
        """
        Restituisce una lista di farmaci suggeriti di un determinato tipo, escludendo il farmaco con l'ID specificato.

        Args:
            tipo (str): Il tipo di farmaci da suggerire.
            id (int): L'ID del farmaco da escludere dalla lista dei suggerimenti.

        Returns:
            list: Una lista di farmaci suggeriti.
        """
        return db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.categoria==tipo, Farmaco.ID != id)).fetchall()
    @classmethod
    def filtraCatalogo(cls,categoria = None, prezzo=0):
        """
        Filtra il catalogo dei farmaci in base alla categoria e/o al prezzo.

        Args:
            categoria (str): La categoria di farmaci da mostrare. Se None, mostra tutti i farmaci.
            prezzo (float): Il massimo prezzo del farmaco da mostrare. Se 0, non filtra per prezzo.

        Returns:
            list: Una lista di farmaci filtrati in base alla categoria e/o al prezzo.
        """
        if categoria == "-" and prezzo == 0 :
            return list(db.session.scalars(sqlalchemy.select(Farmaco)))
        elif categoria == "-" and prezzo != 0 :
            return list(db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.prezzo <= prezzo)))
        elif categoria != "-" and prezzo == 0:
            return list(db.session.scalars(sqlalchemy.select(Farmaco).where(Farmaco.categoria==categoria)))
        else:
            return cls.getFarmaci()

    @classmethod
    def ricerca(cls,tip=None):
        """
        Restituisce una lista di suggerimenti di farmaci basati sulla ricerca per nome.

        Args:
            tip (str): Il suggerimento di ricerca.

        Returns:
            list: Una lista di suggerimenti di farmaci.
        """
        if tip is not None and tip!="":
            suggerimenti={farmaco.nome for farmaco in Farmaco.query.filter(Farmaco.nome.like(tip+'%')).all()}
            suggest=list(suggerimenti)
            return suggest

    @classmethod
    def ricercaNome(cls, nome=None):
        """
        Restituisce una lista di farmaci filtrati per nome.

        Args:
            nome (str): Il nome del farmaco da cercare.

        Returns:
            list: Una lista di farmaci filtrati per nome.
        """
        if nome is not None:
            return Farmaco.query.filter(Farmaco.nome.like(nome+'%')).all()





