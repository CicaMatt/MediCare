from flaskDir.source.ModuloIA.DataPreparation import df, train, predict
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

trainset = df[train]
X_train, X_val, y_train, y_val = train_test_split(trainset, predict, test_size=0.2, random_state=42)
print("KNN")
modello = KNeighborsClassifier(n_neighbors=43)
modello.fit(X_train, y_train)
y_pred = modello.predict(X_val)
print(classification_report(y_val, y_pred))
matrice = confusion_matrix(y_val, y_pred)

print("SVM")

modello2 = SVC(kernel='linear')
modello2.fit(X_train, y_train)
y_pred = modello2.predict(X_val)
print(classification_report(y_val, y_pred))

print("DC")
modello3 = DecisionTreeClassifier(criterion='entropy')
modello3.fit(X_train, y_train)
y_pred = modello3.predict(X_val)
print(classification_report(y_val, y_pred))
