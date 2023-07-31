%pip install seaborn
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("cust_data.csv")

sns.jointplot(x="avg_bill", y="age", data=df)
plt.show()

sns.jointplot(x="avg_bill", y="age", data=df, kind='hex')
plt.show()