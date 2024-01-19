from flaskDir.source.ModuloIA import df, pd
from scipy import stats
from scipy.stats._mstats_basic import winsorize

winsorize_percentile_oldpeak = (stats.percentileofscore(df['oldpeak'], 4) / 100)
old_peak_winsorize = winsorize(df['oldpeak'], (0, (1 - winsorize_percentile_oldpeak)))
df['oldpeak'] = old_peak_winsorize

winsorize_percentile_trtbps = (stats.percentileofscore(df['trtbps'], 170) / 100)
trtbps_winsorize = winsorize(df['trtbps'], (0, (1 - winsorize_percentile_trtbps)))
df['trtbps'] = trtbps_winsorize

winsorize_percentile_chol = (stats.percentileofscore(df['chol'], 360) / 100)
chol_winsorize = winsorize(df['chol'], (0, (1 - winsorize_percentile_chol)))
df['chol'] = chol_winsorize

# Si parte con la feature scaling
# Normalizziamo l'età
prev = df['age']
min_prev = prev.min()
max_eta = prev.max()

normale = (prev - min_prev) / (max_eta - min_prev)
df['age'] = normale

# Normalizziamo thalach
prev = df['thalachh']
min_prev = prev.min()
max_prev = prev.max()

normale = (prev - min_prev) / (max_prev - min_prev)

df['thalachh'] = normale

print(df['thalachh'])

# Normalizziamo OldPeak
prev = df['oldpeak']
min_prev = prev.min()
max_prev = prev.max()

normale = (prev - min_prev) / (max_prev - min_prev)

df['oldpeak'] = normale

print(df['oldpeak'])

# Normalizziamo trtbps
prev = df['trtbps']
min_prev = prev.min()
max_prev = prev.max()

normale = (prev - min_prev) / (max_prev - min_prev)

df['trtbps'] = normale
print(df['trtbps'])

# Normalizziamo il colesterolo
prev = df['chol']
min_prev = prev.min()
max_prev = prev.max()

normale = (prev - min_prev) / (max_prev - min_prev)
df['chol'] = normale
print(df['chol'])

# Cancelliamo i dati non disponibili
df = df.drop(['caa', 'thall', 'slp'], axis=1)

# Normalizziamo le categoriche con OneHotEncode
colonne_cat = ['sex', "cp", 'fbs', 'restecg', 'exng']

df = pd.get_dummies(df, columns=colonne_cat, prefix=colonne_cat)
print(df)

train = df.columns.tolist()
print(train)
train.remove('HeartDisease')
predict = df['HeartDisease'].values
