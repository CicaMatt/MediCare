from flaskDir import db, app
from sqlalchemy import text
class MetodoPagamentoDAO():
    __table="metodopagamento"
    @classmethod
    def doSave(cls, metodoPagamento):
        query = text("INSERT INTO "+cls.__table+" VALUES (:cvv,:pan,:nome_titolare, :data_scadenza, :beneficiario)")
        beneficiario=metodoPagamento.getBeneficiario().getCF()
        if MetodoPagamentoDAO.findByKey(beneficiario, metodoPagamento.getPAN()) is None:
            with app.app_context():
                db.session.execute(query,{"cvv":metodoPagamento.cvv,"nome_titolare": metodoPagamento.nome_titolare,
                                          "data_scadenza":metodoPagamento.data_scadenza, "beneficiario": beneficiario})
                db.session.commit()
            return True
        return False

    @classmethod
    def doUpdate(cls,old_metodo,new_metodo):
        query=text("UPDATE "+cls.__table+" set CVV=:cvv, nometitolare=:tit, PAN=:pan,dataScadenza=:data, beneficiario=:ben where PAN=:oldpan and"
                                         +" beneficiario=:oldben")
        beneficiario = new_metodo.getBeneficiario().getCF()
        old_ben = old_metodo.getBeneficiario().getCF()
        if MetodoPagamentoDAO.findByKey(beneficiario, new_metodo.getPAN()) is not None:
            with app.app_context():
                db.session.execute(query, {"cvv": new_metodo.getCVV(), "nome_titolare": new_metodo.getTitolare(), "pan": new_metodo.getPAN(),
                                          "data_scadenza": new_metodo.getDataScadenza(), "beneficiario":beneficiario, "oldpan":old_metodo.getPAN(),
                                          "oldben":old_ben})
                db.session.commit()
            return True
        return False

    @classmethod
    def doDelete(cls,pan,beneficiario):
        query=text("DELETE FROM "+cls.__table+" WHERE PAN=:pan and beneficiario=:ben")
        if cls.findByKey(pan,beneficiario) is not None:
            with app.app_context():
                db.session.execute(query, {"pan":pan, "beneficiario":beneficiario})
                db.session.commit()
            return True
        return False

    @classmethod
    def findByKey(cls,beneficiario=None, numero_carta=None):
        query=text("Select * from "+cls.__table+" where beneficiario=:bene and PAN=:carta")
        if numero_carta is not None and beneficiario is not None:
            with app.app_context():
                return db.session.execute(query,{"bene":beneficiario, "carta":numero_carta}).first()

    @classmethod
    def findAll(cls):
        query = text("Select * from "+cls.__table)
        with app.app_context():
            return db.session.execute(query)

    @classmethod
    def findByBeneficiario(cls, beneficiario=None):
        query = text("Select * from "+cls.__table+" where beneficiario=:ben")
        if beneficiario is not None:
            with app.app_context():
                return db.session.execute(query, {"ben": beneficiario}).all()




