from flaskDir.source.ModuloIA.DataPreparation import df,train,predict
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

print(len(df))

modello=KNeighborsClassifier(n_neighbors=10)
modello2=SVC(kernel='linear')
modello3=DecisionTreeClassifier()

kfold= StratifiedKFold(n_splits=8,shuffle=True, random_state=42)
risultati_cross_val = cross_val_score(modello, train, predict, cv=kfold, scoring='accuracy')

print(risultati_cross_val)
risultati_cross_val = cross_val_score(modello2, train, predict, cv=kfold, scoring='accuracy')

print(risultati_cross_val)
risultati_cross_val = cross_val_score(modello3, train, predict, cv=kfold, scoring='accuracy')
print(risultati_cross_val)