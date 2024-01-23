from sklearn.svm import SVC

from flaskDir.source.ModuloIA.DataPreparation import df, predict
from flaskDir.source.ModuloIA.DataPreparation2 import df as df_simple
from flaskDir.source.ModuloIA.DataPreparation2 import train as simple

modelloAccurato = SVC(kernel='linear')
modelloAccurato.fit(df, predict)

modelloSimple = SVC(kernel='linear')
modelloSimple.fit(df_simple[simple], predict)
