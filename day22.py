%matplotlib inline
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

plt.figure()
plt.plot(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], [28,30,29,31,32,31,31] )
plt.show()

plt.figure()
plt.plot(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], [28,30,29,31,32,31,31] )
plt.xlabel('Day')
plt.ylabel('Temp')
plt.title('High Temperature')
plt.show()

fm.findSystemFonts(fontpaths=None, fontext='ttf')

plt.rc('font', family='NanumGothicCoding')
plt.rc('axes', unicode_minus=False)

plt.plot(["월","화","수","목","금","토","일"], [28,30,29,31,32,31,31] )
plt.xlabel('일')
plt.ylabel('온도')
plt.title('일별 최고 기온')
plt.show()

plt.plot([1,2,3], [1,4,9])
plt.plot([2,3,4],[5,6,7])
plt.xlabel('Quarter')
plt.ylabel('Score')
plt.title('Game Result')
plt.legend(['A team', 'B team'])
plt.show()

plt.plot([1,2,3],[1,4,9],[2,3,4],[5,6,7])
plt.xlabel('Quarter')
plt.ylabel('Score')
plt.title('Game Result')
plt.legend(['A team', 'B team'])
plt.show()

x=list(range(0,10))
y1=list(range(0,10))
y2=list(range(0,20,2))
y3=list(range(0,40,4))

plt.plot(x,y1,x,y2, x, y3)
plt.show()

plt.plot(x,y1,'r--', x,y2, 'bs' ,x, y3, 'g^:')
plt.show()

x=list(range(0,10))
y1=[0,1,2,3,4,5,6,7,8,9]
y2=[0,1,4,9,16,25,36,49,64,81]

plt.figure()
plt.plot(x,y1)
plt.figure()
plt.plot(x,y2)

plt.show()

plt.figure(figsize=(20,12))

plt.subplot(221)
plt.subplot(222)
plt.subplot(212)

plt.show()

plt.figure(figsize=(20,12))

plt.subplot(221)
plt.plot([1,2,3], [110,130,120])
plt.grid()

plt.subplot(222)
plt.plot(["월","화","수","목","금","토","일"], [28,30,29,31,32,31,31] )
plt.xlabel('요일')
plt.ylabel('기온')
plt.title('최고기온')
plt.grid()

plt.subplot(212)
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.barh(x, y, height=0.7, color="red")
plt.grid()

plt.show()