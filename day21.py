%matplotlib inline
import matplotlib.pyplot as plt

plt.figure()
plt.plot([1,2,3], [100,120,110])
plt.show()

plt.figure(figsize=(16,5))
plt.plot([1,2,3], [100,120,110])
plt.show()

plt.figure()
plt.plot(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], [28,30,29,31,32,31,31] )
plt.show()

import pandas as pd
df=pd.read_csv("cust_data.csv")
df.head()

df.plot()
plt.show()

df['avg_bill'].plot(figsize=(50,30))
plt.show()

plt.figure(figsize=(16,6))
plt.scatter(y=df["avg_bill"], x=df["age"])
plt.show()

plt.figure()
plt.hist(df["A_bill"])
plt.show()

plt.figure()
plt.hist(df["age"],bins=20)
plt.show()

x=[5, 3, 7, 10, 9, 5, 3.5, 8]

plt.boxplot(x=x)
plt.show()

df.boxplot(by="by_age", column="avg_bill", figsize=(16,8))
plt.show()

y=[5, 3, 7, 10, 9, 5, 3.5, 8]
x=list(range(len(y)))

plt.figure()
plt.bar(x, y)
plt.show()

df2=pd.pivot_table(df, index = ['service'])
print(df2)

df2[['A_bill', 'B_bill']].plot(kind='bar')

df2[['A_bill', 'B_bill']].plot(kind='bar', stacked=True)