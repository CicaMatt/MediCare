from flaskDir.source.ModuloIA import df,pd

#Si parte con la feature scaling
#Normalizziamo l'età
prev=df['age']
min_prev=prev.min()
max_eta=prev.max()

normale=(prev-min_prev)/(max_eta-min_prev)
df['age']=normale


#Normalizziamo thalach
prev=df['thalachh']
min_prev=prev.min()
max_prev=prev.max()

normale=(prev-min_prev)/(max_prev-min_prev)

df['thalachh']=normale

print(df['thalachh'])

#Normalizziamo OldPeak
prev=df['oldpeak']
min_prev=prev.min()
max_prev=prev.max()

normale=(prev-min_prev)/(max_prev-min_prev)

df['oldpeak']=normale

print(df['oldpeak'])

#Normalizziamo trtbps
prev=df['trtbps']
min_prev=prev.min()
max_prev=prev.max()

normale=(prev-min_prev)/(max_prev-min_prev)

df['trtbps']=normale
print(df['trtbps'])

#Normalizziamo il colesterolo
prev=df['chol']
min_prev=prev.min()
max_prev=prev.max()

normale=(prev-min_prev)/(max_prev-min_prev)
df['chol']=normale
print(df['chol'])


#Cancelliamo i dati non disponibili
df=df.drop(['caa','thall','slp'], axis=1)

#Normalizziamo le categoriche con OneHotEncode
colonne_cat=['sex',"cp",'fbs','restecg','exng']

df=pd.get_dummies(df,columns=colonne_cat, prefix=colonne_cat)
print(df)

train=df.columns.tolist()
print(train)
train.remove('HeartDisease')
predict=df['HeartDisease'].values