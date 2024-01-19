import graphviz
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, ConfusionMatrixDisplay
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from flaskDir.source.ModuloIA.DataPreparation import df, np, train, predict

acc_log = []
"""
heart_disease_count = df['HeartDisease'].value_counts()
heart_disease_percentage = heart_disease_count / df.shape[0] * 100

# Plotting the prevalence
plt.figure(figsize=(8, 6))
sns.barplot(x=heart_disease_count.index, y=heart_disease_count.values)
plt.title("Prevalenza della Malattia Cardiaca")
plt.xlabel("Malattia (0 = No, 1 = Si)")
plt.ylabel("Numero di individui")
plt.xticks([0, 1], ['Nessuna Malattia Cardiaca', 'Malattia Cardiaca'])

# Displaying percentages
for index, value in enumerate(heart_disease_count):
    plt.text(index, value, f'{heart_disease_percentage[index]:.2f}%', ha='center')

plt.show()"""

kfold = StratifiedKFold(n_splits=7, shuffle=True, random_state=25)
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
    disp = ConfusionMatrixDisplay(confusion_matrix=matrice)
    disp.plot()
    plt.show()
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
    disp = ConfusionMatrixDisplay(confusion_matrix=matrice)
    disp.plot()
    plt.show()
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
    disp = ConfusionMatrixDisplay(confusion_matrix=matrice)
    disp.plot()
    plt.show()
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
    plt.figure(figsize=(20, 15))
    importance = modello3.feature_importances_
    idxs = np.argsort(importance)
    plt.title("Importanza delle feature - Albero Decisionale")
    plt.barh(range(len(idxs)), importance[idxs], align="center")
    plt.yticks(range(len(idxs)), [train[i] for i in idxs])
    plt.xlabel("Decision Tree Feature Importance")
    plt.show()
    dot_data = tree.export_graphviz(modello3, out_file=None,
                                    feature_names=train,
                                    class_names='HeartDisease',
                                    filled=True)
    graph = graphviz.Source(dot_data, format="png")
    graph.render("decision_tree")
    graph.view("decision_tree")
