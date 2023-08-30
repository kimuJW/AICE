!pip install factor-analyzer
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo

df.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE'],axis=1)
kmo_all,kmo_model=calculate_kmo(df.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE'],axis=1))
kmo_model

fa = FactorAnalyzer()
fa.set_params(rotation=None)
fa.fit(df.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE'],axis=1))
ev, v = fa.get_eigenvalues()
ev

plt.scatter(range(1,df.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE'],axis=1).shape[1]+1),ev)
plt.plot(range(1,df.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE'],axis=1).shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

fa = FactorAnalyzer()
fa.set_params(n_factors=3, rotation=None)
fa.fit(df.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE'],axis=1))
pd.DataFrame(fa.loadings_)

plt.figure(figsize=(6,10))
sns.heatmap(fa.loadings_, cmap="Blues", annot=True, fmt='.2f')

def CronbachAlpha(itemscores):
    itemscores = np.asarray(itemscores)
    itemvars = itemscores.var(axis=0, ddof=1)
    tscores = itemscores.sum(axis=1)
    nitems = itemscores.shape[1]
    return (nitems / (nitems-1)) * (1 - (itemvars.sum() / tscores.var(ddof=1)))

print(CronbachAlpha(df[['ET','ETA']]))

print(CronbachAlpha(df[['ET','A_DISTANCE']]))

fa.transform(df.drop(['RID','TIME_DEPARTUREDATE','TIME_ARRIVEDATE'],axis=1))