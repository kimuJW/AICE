%pip install seaborn
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("cust_data.csv")

sns.catplot(x='age', y='avg_bill',data=df ,col="class", col_wrap=2)
plt.show()

plt.figure(figsize=(10,5))
sns.lmplot(x='avg_bill', y='B_bill', data=df,line_kws={'color': 'red'})
plt.show()

sns.lmplot(x='avg_bill', y='B_bill', data=df, hue='sex')
plt.show()