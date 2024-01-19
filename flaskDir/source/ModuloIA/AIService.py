import pandas as pd

from flaskDir.source.ModuloIA.DataPreparation import df as df_accurato
from flaskDir.source.ModuloIA.DataPreparation import df as df_simple
from flaskDir.source.ModuloIA.DataPreparation import min_eta, max_eta, min_thal, max_thal, min_oldpeak, max_oldpeak, \
    min_chol, max_chol, min_trtbps, max_trtbps, colonne_cat
from flaskDir.source.ModuloIA.DataPreparation2 import colonne_cat as colonne_simple
from flaskDir.source.ModuloIA.Modello_definitivo import modelloAccurato, modelloSimple


class ModuloIAService:
    @classmethod
    def diagnosi_accurata(cls, age, sex, cp, trtbps, chol, fbs, restecg, thalach, exng, oldpeak, slp, caa, thall):
        new_istance = pd.DataFrame(
            {'age': age, 'sex': sex, 'cp': cp, 'trtbps': trtbps, 'chol': chol, 'fbs': fbs, 'restecg': restecg,
             'thalachh': thalach
                , 'exng': exng, 'oldpeak': oldpeak, 'slp': slp, 'caa': caa, 'thall': thall}, index=[0])
        new_istance['age'] = (age - min_eta) / (max_eta - min_eta)
        new_istance['thalachh'] = (thalach - min_thal) / (max_thal - min_thal)
        new_istance['oldpeak'] = (oldpeak - min_oldpeak) / (max_oldpeak - min_oldpeak)
        new_istance['chol'] = (chol - min_chol) / (max_chol - min_chol)
        new_istance['trtbps'] = (trtbps - min_trtbps) / (max_trtbps - min_trtbps)

        new_istance = pd.get_dummies(new_istance, columns=colonne_cat, prefix=colonne_cat)
        colonne_mancanti = set(df_accurato.columns) - set(new_istance.columns)
        for col in colonne_mancanti:
            new_istance[col] = 0
        new_istance.columns.drop('HeartDisease')
        colonne = df_accurato.columns.tolist()
        new_istance = new_istance.reindex(columns=colonne)
        print(new_istance.columns)
        result = modelloAccurato.predict(new_istance)
        return result

    @classmethod
    def diagnosi_simple(cls, age, sex, cp, trtbps, chol, fbs, restecg, thalach, exng, oldpeak):
        new_istance = pd.DataFrame(
            {'age': age, 'sex': sex, 'cp': cp, 'trtbps': trtbps, 'chol': chol, 'fbs': fbs, 'restecg': restecg,
             'thalachh': thalach
                , 'exng': exng, 'oldpeak': oldpeak}, index=[0])
        new_istance['age'] = (age - min_eta) / (max_eta - min_eta)
        new_istance['thalachh'] = (thalach - min_thal) / (max_thal - min_thal)
        new_istance['oldpeak'] = (oldpeak - min_oldpeak) / (max_oldpeak - min_oldpeak)
        new_istance['chol'] = (chol - min_chol) / (max_chol - min_chol)
        new_istance['trtbps'] = (trtbps - min_trtbps) / (max_trtbps - min_trtbps)
        new_istance = pd.get_dummies(new_istance, columns=colonne_simple, prefix=colonne_simple)
        colonne_mancanti = set(df_simple.columns) - set(new_istance.columns)
        for col in colonne_mancanti:
            new_istance[col] = 0
        result = modelloSimple.predict(new_istance)
        return result
