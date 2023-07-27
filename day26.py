%matplotlib inline
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

plt.figure(figsize=(20,5))

plt.subplot(121)
plt.plot(df2['avg_bill'],'rs-')


plt.subplot(122)
plt.hist(df['age'], bins=20)
plt.xlabel('나이')
plt.ylabel('고객수')

plt.figure(figsize=(20,10))
plt.scatter(x=df['age'], y=df['avg_bill'], c='green')

plt.show()