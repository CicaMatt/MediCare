from flaskDir.source.ModuloIA import DataPreparation2
from flaskDir.source.ModuloIA.DataPreparation import df,train,predict

from sklearn.svm import SVC

modelloAccurato=SVC(kernel='linear')
modelloAccurato.fit(train,predict)

modelloSimple=SVC(kernel='linear')
modelloSimple.fit(DataPreparation2.train, DataPreparation2.predict)