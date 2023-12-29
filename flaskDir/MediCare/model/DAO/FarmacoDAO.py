from flaskDir import db, app
from sqlalchemy import text
from flaskDir.MediCare.model.entity.Farmaco import Farmaco
class FarmacoDAO():
    __table="farmaco"


    @classmethod
    def doSave(cls,farmaco: Farmaco)->bool:
        query = text("INSERT INTO "+cls.__table+"(prezzo,nome,categoria,descrizione) VALUES(:prezzo, :nome, :categoria,:descrizione)")
        if cls.findById(farmaco.getId()) is None and cls.findByUnique(farmaco.getNome(),farmaco.getCategoria()) is None:
            with app.app_context():
                db.session.execute(query,{"prezzo":farmaco.getPrezzo(), "nome":farmaco.getNome(),
                                          "categoria":farmaco.getCategoria(),"descrizione":farmaco.getDescrizione()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doUpdate(cls,old_id:int,new_farmaco:Farmaco)->bool:
        query = text("UPDATE "+cls.__table+" SET prezzo=:prezzo, nome=:nome, categoria=:cat, descrizione=:descrizione WHERE ID=:id")
        if cls.findById(old_id) is not None and cls.findByUnique(new_farmaco.getId(),new_farmaco.getCategoria()) is None:
            with app.app_context():
                db.session.execute(query,{"prezzo": new_farmaco.getPrezzo(), "nome": new_farmaco.getNome(),
                                          "cat":new_farmaco.getCategoria(), "descrizione": new_farmaco.getDescrizione()})
                db.session.commit()
            return True
        return False

    @classmethod
    def doDelete(cls,id:int)->bool:
        query = text("DELETE FROM "+cls.__table+" WHERE ID=:id")
        if cls.findById(id) is not None:
            with app.app_context():
                db.session.execute(query, {"id": id})
                db.session.commit()
            return True
        return False


    @classmethod
    def findById(cls, id:int)->Farmaco:
        query = text("Select * from "+cls.__table+" where ID=:id")
        with app.app_context():
            res = db.session.execute(query,{"id": id}).first()
            if res is not None:
                farmaco=Farmaco(*res)
                return farmaco


    @classmethod
    def findAll(cls)->list:
        query = text("SELECT * from "+cls.__table)
        farmaci = list()
        with app.app_context():
            res = db.session.execute(query).all()
            if res is not None:
                farmaco=Farmaco(*res)
                farmaci.append(farmaco)
        return farmaci

    @classmethod
    def findByUnique(cls,nome=None,categoria=None)->Farmaco:
        query = text("SELECT * from "+cls.__table+" where nome=:nome and categoria=:cat")
        if nome is not None and categoria is not None:
            with app.app_context():
                res = db.session.execute(query, {"nome":nome, "cat":categoria}).first()
                if res is not None:
                    farmaco=Farmaco(*res)
                    return farmaco
    @classmethod
    def findByCategoria(cls,categoria=None)->list:
        query = text("SELECT * from "+cls.__table+" where  categoria=:cat")
        farmacifitr=list()
        if categoria is not None:
            with app.app_context():
                res = db.session.execute(query,{"cat":categoria})
                if res is not None:
                    for row in res:
                        farmaco=Farmaco(*row)
                        farmacifitr.append(farmaco)
        return farmacifitr

    @classmethod
    def findByNome(cls,nome=None)->list:
        query = text("Select * from "+cls.__table+" where nome:nome")
        farmacifiltr=list()
        if nome is not None:
            with app.app_context():
                res = db.session.execute(query, {"nome": nome})
                if res is not None:
                    for row in res:
                        farmaco=Farmaco(*row)
                        farmacifiltr.append(farmaco)
        return farmacifiltr

