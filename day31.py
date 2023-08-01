%pip install seaborn
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("cust_data.csv")
df.corr()
plt.rc('axes', unicode_minus=False)
sns.heatmap(df.corr())
plt.show()