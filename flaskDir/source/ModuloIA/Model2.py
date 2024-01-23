from flaskDir.source.ModuloIA.DataPreparation2 import df, train, predict
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

acc_log = []

kfold = StratifiedKFold(n_splits=7, shuffle=True, random_state=42)
print("KNN")
for fold, (train_index, val_index) in enumerate(kfold.split(X=df, y=predict)):
    X_train = df.loc[train_index, train]
    Y_train = df.loc[train_index, 'HeartDisease']

    X_val = df.loc[val_index, train]
    Y_val = df.loc[val_index, 'HeartDisease']

    modello = KNeighborsClassifier(n_neighbors=10)
    modello.fit(X_train, Y_train)
    y_pred = modello.predict(X_val)
    print(f"The fold is : {fold} : ")
    print(classification_report(Y_val, y_pred))
    acc = roc_auc_score(Y_val, y_pred)
    acc_log.append(acc)
    print(f"The accuracy for Fold {fold + 1} : {acc}")
    matrice = confusion_matrix(Y_val, y_pred)
    print(f"The confusion matrix for Fold {fold + 1}")
    print(matrice)

acc_log = []
print("SVM")
for fold, (train_index, val_index) in enumerate(kfold.split(X=df, y=predict)):
    X_train = df.loc[train_index, train]
    Y_train = df.loc[train_index, 'HeartDisease']

    X_val = df.loc[val_index, train]
    Y_val = df.loc[val_index, 'HeartDisease']

    modello2 = SVC(kernel='linear')
    modello2.fit(X_train, Y_train)
    y_pred = modello2.predict(X_val)
    print(f"The fold is : {fold + 1} : ")
    print(classification_report(Y_val, y_pred))
    acc = roc_auc_score(Y_val, y_pred)
    acc_log.append(acc)
    print(f"The accuracy for Fold {fold + 1} : {acc}")
    matrice = confusion_matrix(Y_val, y_pred)
    print(f"The confusion matrix for Fold {fold + 1}")
    print(matrice)

acc_log = []
print("DC")
for fold, (train_index, val_index) in enumerate(kfold.split(X=df, y=predict)):
    X_train = df.loc[train_index, train]
    Y_train = df.loc[train_index, 'HeartDisease']

    X_val = df.loc[val_index, train]
    Y_val = df.loc[val_index, 'HeartDisease']

    modello3 = DecisionTreeClassifier(criterion='entropy')
    modello3.fit(X_train, Y_train)
    y_pred = modello3.predict(X_val)
    print(f"The fold is : {fold + 1} : ")
    print(classification_report(Y_val, y_pred))
    acc = roc_auc_score(Y_val, y_pred)
    acc_log.append(acc)
    print(f"The accuracy for Fold {fold + 1} : {acc}")
    matrice = confusion_matrix(Y_val, y_pred)
    print(f"The confusion matrix for Fold {fold + 1}")
    print(matrice)

acc_log = []

kfold = StratifiedKFold(n_splits=9, shuffle=True, random_state=42)
print("KNN")
for fold, (train_index, val_index) in enumerate(kfold.split(X=df, y=predict)):
    X_train = df.loc[train_index, train]
    Y_train = df.loc[train_index, 'HeartDisease']

    X_val = df.loc[val_index, train]
    Y_val = df.loc[val_index, 'HeartDisease']

    modello = KNeighborsClassifier(n_neighbors=10)
    modello.fit(X_train, Y_train)
    y_pred = modello.predict(X_val)
    print(f"The fold is : {fold + 1} : ")
    print(classification_report(Y_val, y_pred))
    acc = roc_auc_score(Y_val, y_pred)
    acc_log.append(acc)
    print(f"The accuracy for Fold {fold + 1} : {acc}")
    matrice = confusion_matrix(Y_val, y_pred)
    print(f"The confusion matrix for Fold {fold + 1}")
    print(matrice)

acc_log = []
print("SVG")
for fold, (train_index, val_index) in enumerate(kfold.split(X=df, y=predict)):
    X_train = df.loc[train_index, train]
    Y_train = df.loc[train_index, 'HeartDisease']

    X_val = df.loc[val_index, train]
    Y_val = df.loc[val_index, 'HeartDisease']

    modello2 = SVC(kernel='linear')
    modello2.fit(X_train, Y_train)
    y_pred = modello2.predict(X_val)
    print(f"The fold is : {fold + 1} : ")
    print(classification_report(Y_val, y_pred))
    acc = roc_auc_score(Y_val, y_pred)
    acc_log.append(acc)
    print(f"The accuracy for Fold {fold + 1} : {acc}")
    matrice = confusion_matrix(Y_val, y_pred)
    print(f"The confusion matrix for Fold {fold + 1}")
    print(matrice)

acc_log = []
print("DC")
for fold, (train_index, val_index) in enumerate(kfold.split(X=df, y=predict)):
    X_train = df.loc[train_index, train]
    Y_train = df.loc[train_index, 'HeartDisease']

    X_val = df.loc[val_index, train]
    Y_val = df.loc[val_index, 'HeartDisease']

    modello3 = DecisionTreeClassifier(criterion='entropy')
    modello3.fit(X_train, Y_train)
    y_pred = modello3.predict(X_val)
    print(f"The fold is : {fold + 1} : ")
    print(classification_report(Y_val, y_pred))
    acc = roc_auc_score(Y_val, y_pred)
    acc_log.append(acc)
    print(f"The accuracy for Fold {fold + 1} : {acc}")
    matrice = confusion_matrix(Y_val, y_pred)
    print(f"The confusion matrix for Fold {fold + 1}")
    print(matrice)
