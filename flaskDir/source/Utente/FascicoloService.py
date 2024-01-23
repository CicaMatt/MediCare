from datetime import datetime

import sqlalchemy
import datetime
from flaskDir import app, db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario


class FascicoloService:
    """
    Classe che fornisce tutti i metodi relativi alla visualizzazione e modifica del
    fascicolo sanitario elettronico.
    """
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
    def addDocumento(cls, tipo, descrizione, richiamo, codicefiscale):
        """
        Aggiunge un nuovo documento sanitario al fascicolo di un paziente.

        Args:
            tipo (str): Tipo del documento sanitario.\n
            descrizione (str): Descrizione del documento.\n
            richiamo (str): Informazioni sul richiamo associato al documento.\n
            codicefiscale (str): Codice fiscale del paziente.\n

        Returns:
            None
        """
        with app.app_context():
            documento = DocumentoSanitario()
            quantidocumenti = len(list(db.session.scalars(
                sqlalchemy.select(DocumentoSanitario).where(DocumentoSanitario.titolare == codicefiscale))))
            documento.NumeroDocumento = "FSE" + str(quantidocumenti) + tipo[0]
            documento.tipo = tipo
            documento.dataEmissione = datetime.date.today()
            documento.descrizione = descrizione
            documento.richiamo = richiamo
            documento.titolare = codicefiscale
            db.session.add(documento)
            db.session.commit()
