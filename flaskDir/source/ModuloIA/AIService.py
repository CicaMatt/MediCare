from flaskDir.source.ModuloIA.Modello_definitivo import modelloAccurato, modelloSimple
from flaskDir.source.ModuloIA.DataPreparation import min_eta,max_eta,min_thal,max_thal,min_oldpeak,max_oldpeak,min_chol,max_chol,min_trtbps, max_trtbps, colonne_cat
from flaskDir.source.ModuloIA.DataPreparation2 import colonne_cat as colonne_simple
import pandas as pd
class ModuloIAService:
    @classmethod
    def diagnosi_acurrata(cls,age,sex,cp,trtbps,chol,fbs,restecg,thalach,exng,oldpeak,slp,caa,thall):
        new_istance=pd.DataFrame({'age':age,'sex':sex,'cp':cp,'trtbps':trtbps,'chol':chol,'fbs':fbs,'restecg':restecg,'thalachh':thalach
                                  ,'exng':exng,'oldpeak':oldpeak,'slp':slp,'caa':caa,'thall':thall})
        new_istance['age']=(age-min(age))/(max_eta-min_eta)
        new_istance['thalachh']=(thalach-min_thal)/(max_thal-min_thal)
        new_istance['oldpeak']=(oldpeak-min(oldpeak))/(max_oldpeak-min_oldpeak)
        new_istance['chol']=(chol-min_chol)/(max_chol-min_chol)
        new_istance['trtbps']=(trtbps-min(trtbps))/(max_trtbps-min_trtbps)
        new_istance=pd.get_dummies(new_istance,columns=colonne_cat,prefix=colonne_cat)
        result=modelloAccurato.predict(new_istance)



    @classmethod
    def diagnosi_simple(cls,age,sex,cp,trtbps,chol,fbs,restecg,thalach,exng,oldpeak):
        new_istance = pd.DataFrame(
            {'age': age, 'sex': sex, 'cp': cp, 'trtbps': trtbps, 'chol': chol, 'fbs': fbs, 'restecg': restecg,
             'thalachh': thalach
                , 'exng': exng, 'oldpeak': oldpeak})
        new_istance['age'] = (age - min(age)) / (max_eta - min_eta)
        new_istance['thalachh'] = (thalach - min_thal) / (max_thal - min_thal)
        new_istance['oldpeak'] = (oldpeak - min(oldpeak)) / (max_oldpeak - min_oldpeak)
        new_istance['chol'] = (chol - min_chol) / (max_chol - min_chol)
        new_istance['trtbps'] = (trtbps - min(trtbps)) / (max_trtbps - min_trtbps)
        new_istance = pd.get_dummies(new_istance, columns=colonne_simple, prefix=colonne_simple)
        result = modelloAccurato.predict(new_istance)