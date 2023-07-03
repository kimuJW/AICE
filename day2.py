a = ['red', 'green', 'blue']
a.append('yellow')
a.insert(1, 'black')
b = ['purple', 'white']
a.extend(b)
c = a+b
d = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
d.remove(90)
d.pop(0)
list1 = ['a', 'bb', 'c', 'd','aaa', 'c', 'ddd', 'aaa',  'b', 'cc', 'd', 'aaa', ]
list2 = [1, -7, 5, 8, 3, 9, 11, 13]
list2.sort(reverse=True)

print(a)
print(b)
print(c)
print(d)
list1.count('aaa')
list2