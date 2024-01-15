from flaskDir.source.ModuloIA.DataPreparation2 import train as simple
from flaskDir.source.ModuloIA.DataPreparation2 import df as df_simple
from flaskDir.source.ModuloIA.DataPreparation import df,train,predict

from sklearn.svm import SVC

modelloAccurato=SVC(kernel='linear')
modelloAccurato.fit(df[train],predict)

modelloSimple=SVC(kernel='linear')
modelloSimple.fit(df_simple[simple], predict)