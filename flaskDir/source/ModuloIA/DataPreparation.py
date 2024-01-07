from flaskDir.source.ModuloIA import df,pd,np,plt

fig, (primo,secondo,terzo,quarto)=plt.subplots(1,4,figsize=(28,6))

primo.boxplot(df['age'])
primo.set_title("age")

secondo.boxplot(df['trtbps'])
secondo.set_title("trtbps")

terzo.boxplot(df['thalachh'])
terzo.set_title("thalach")

quarto.boxplot(df['oldpeak'])
quarto.set_title("oldpeak")

plt.show()


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

df['thalach']=normale

print(df['thalach'])

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


#Normalizziamo le categoriche con OneHotEncode
colonne_cat=['sex',"cp",'fbs','restecg','exng','slp','caa','thall']

df=pd.get_dummies(df,columns=colonne_cat, prefix=colonne_cat)
print(df)


