%pip install seaborn
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv("cust_data.csv")
df.head()

sns.scatterplot(x='age', y='avg_bill', data=df)
plt.show()