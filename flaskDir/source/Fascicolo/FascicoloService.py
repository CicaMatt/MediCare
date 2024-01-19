from datetime import datetime

import sqlalchemy
import datetime
from flaskDir import app, db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario


class FascicoloService:

    @classmethod
    def getDocumentiSanitari(cls, cf):
        """
        Restituisce tutti i documenti sanitari associati a un paziente.

        Args:
            cf (str): Codice fiscale del paziente.

        Returns:
            list: Lista dei documenti sanitari associati al paziente.
        """
        return DocumentoSanitario.query.filter_by(titolare=cf)


    @classmethod
    def addDocumento(cls,tipo,descrizione,richiamo,codicefiscale):
        """
        Aggiunge un nuovo documento sanitario al fascicolo di un paziente.

        Args:
            tipo (str): Tipo del documento sanitario.
            descrizione (str): Descrizione del documento.
            richiamo (str): Informazioni sul richiamo associato al documento.
            codicefiscale (str): Codice fiscale del paziente.

        Returns:
            None
        """
        with app.app_context():
            documento=DocumentoSanitario()
            quantiDocumenti = len(list(db.session.scalars(sqlalchemy.select(DocumentoSanitario).where(DocumentoSanitario.titolare == codicefiscale))))
            documento.NumeroDocumento= "FSE"+str(quantiDocumenti)+tipo[0]
            documento.tipo=tipo
            documento.dataEmissione=datetime.date.today()
            documento.descrizione=descrizione
            documento.richiamo=richiamo
            documento.titolare=codicefiscale
            db.session.add(documento)
            db.session.commit()