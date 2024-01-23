import pandas as pd

from flaskDir.source.ModuloIA.DataPreparation import df as df_accurato
from flaskDir.source.ModuloIA.DataPreparation import df as df_simple
from flaskDir.source.ModuloIA.DataPreparation import min_eta, max_eta, min_thal, max_thal, min_oldpeak, max_oldpeak, \
    min_chol, max_chol, min_trtbps, max_trtbps, colonne_cat
from flaskDir.source.ModuloIA.DataPreparation2 import colonne_cat as colonne_simple
from flaskDir.source.ModuloIA.Modello_definitivo import modelloAccurato, modelloSimple


class ModuloIAService:
    """Classe che fornisce i metodi per effettuare una diagnosi cardiaca, utilizza un modello di Intelligenza artificiale
    basato su Machine Learning."""
    @classmethod
    def diagnosi_accurata(cls, age, sex, cp, trtbps, chol, fbs, restecg, thalach, exng, oldpeak, slp, caa, thall):
        """
                Effettua una diagnosi accurata sulla presenza di malattia cardiaca utilizzando il modello accurato.

                Args:
                    age (int): Età del paziente.\n
                    sex (int): Sesso del paziente (0 per femmina, 1 per maschio).\n
                    cp (int): Tipo di dolore al petto.\n
                    trtbps (int): Pressione sanguigna a riposo.\n
                    chol (int): Livello di colesterolo.\n
                    fbs (int): Livello di zucchero nel sangue a digiuno.\n
                    restecg (int): Risultato dell'elettrocardiogramma a riposo.\n
                    thalach (int): Frequenza cardiaca massima raggiunta.\n
                    exng (int): Angina indotta da sforzo.\n
                    oldpeak (int): Depressione del segmento ST indotta dall'esercizio.\n
                    slp (int): Pendenza del segmento ST durante l'esercizio.\n
                    caa (int): Numero di vasi principali colorati al fluorosio.\n
                    thall (int): Tipo di talessemia.\n

                Returns:
                    result: Risultato della diagnosi (0 se non c'è sospetto di malattia cardiaca, 1 altrimenti).
                """
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
        """
                Effettua una diagnosi semplice sulla presenza di malattia cardiaca utilizzando il modello semplice.

                Args:
                    age (int): Età del paziente.\n
                    sex (int): Sesso del paziente (0 per femmina, 1 per maschio).\n
                    cp (int): Tipo di dolore al petto.\n
                    trtbps (int): Pressione sanguigna a riposo.\n
                    chol (int): Livello di colesterolo.\n
                    fbs (int): Livello di zucchero nel sangue a digiuno.\n
                    restecg (int): Risultato dell'elettrocardiogramma a riposo.\n
                    thalach (int): Frequenza cardiaca massima raggiunta.\n
                    exng (int): Angina indotta da sforzo.\n
                    oldpeak (int): Depressione del segmento ST indotta dall'esercizio.\n

                Returns:
                    result: Risultato della diagnosi (0 se non c'è sospetto di malattia cardiaca, 1 altrimenti).
                """
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
