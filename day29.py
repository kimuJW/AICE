%pip install seaborn
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("cust_data.csv")

plt.figure(figsize=(10,5))
sns.countplot(x="by_age", hue="bill_rating", data=df)
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(x="age",bins=20, hue="bill_rating",data=df, multiple='dodge', shrink=0.8)
plt.show()

sns.countplot(y="class", hue="sex", data=df)
plt.show()

sns.countplot(y="class", hue="sex", data=df, palette='spring')
plt.show()