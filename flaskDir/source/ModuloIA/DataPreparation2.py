from flaskDir.source.ModuloIA import df,pd
from sklearn.preprocessing import RobustScaler

scaler=RobustScaler()
numeric_var=['age','trtbps','chol','thalachh','oldpeak']
scaled_data=scaler.fit_transform(df[numeric_var])
print(scaled_data)

df[numeric_var]=scaled_data
print(df)

colonne_cat=['sex',"cp",'fbs','restecg','exng','slp','caa','thall']

df=pd.get_dummies(df,columns=colonne_cat, prefix=colonne_cat)
print(df)

train=df.columns.tolist()
train.remove('HeartDisease')
predict=df['HeartDisease'].values