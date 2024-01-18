from datetime import datetime

import sqlalchemy
import datetime
from flaskDir import app, db
from flaskDir.MediCare.model.entity.DocumentoSanitario import DocumentoSanitario


class FascicoloService:

    @classmethod
    def getDocumentiSanitari(cls, cf):
        return DocumentoSanitario.query.filter_by(titolare=cf)


    @classmethod
    def addDocumento(cls,tipo,descrizione,richiamo,codicefiscale):
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