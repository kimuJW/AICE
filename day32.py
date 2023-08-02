%pip install seaborn
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("cust_data.csv")

plt.figure(figsize=(16,8))
sns.boxplot(y=df["avg_bill"], x=df["by_age"],width=0.9)
plt.show()

plt.figure(figsize=(16,8))
sns.violinplot(y=df["A_bill"], x=df["class"],width=1)
plt.show()