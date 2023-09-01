import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df_total)
plt.show()

df_total[df_total['ET']>15000]

df_total=df_total[df_total['ET']<=15000]
df_total

sns.pairplot(df_total)
plt.show()

df_total['PerHour']=(df_total['A_DISTANCE']/1000)/(df_total['ET']/3600)
df_total.describe()

len(df_total[df_total['PerHour']>130])
df_total=df_total[df_total['PerHour']<=130]
df_total

sns.pairplot(df_total)
plt.show()

df_pnu = pd.read_csv("onenavi_pnu.csv",sep="|") 
df_signal = pd.read_csv("onenavi_signal.csv",sep="|")

df_total=pd.merge(df_total,df_pnu , on="RID")
df_total=pd.merge(df_total,df_signal , on="RID")
df_total

sns.pairplot(df_total)
plt.show()