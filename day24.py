%matplotlib inline
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

x=list(range(0,10))
y1=list(range(0,10))
y2=list(range(0,20,2))
y3=list(range(0,40,4))

plt.plot(x,y1,x,y2, x, y3)
plt.show()

plt.plot(x,y1,'r--', x,y2, 'bs' ,x, y3, 'g^:')
plt.show()