#m = []
#print(type(m))
#m = [1, 2, 1, 3, 5]
#print(len(m)) #- длина списка, индекс последнего элемента "-1"

#вложенные списки
#m = [[5,6], [7,8], ['s','f']]
#m = m * 2
#m [1], m[2] = m[2], m[1]
#print(m)

#m = [[5,6], [7,8], ['s','f']]d
#n = list(range(90))
#print(n)

#n = list(range(10))
#m = []
#for i in n:
 #   if i == 8:
#        continue
 #   m += [i]
#else:
#    print(m)

#x = [9, 8, 7, 6, 5]
#x.append(4)
#x.insert(1,7)
#print(x.count(7))
#x.sort()
#x.reverse()
#y = x.pop(0)
#print(y)
#x.remove(7)
#x.clear()
#x.extend(['a', 's'])
#h = x.copy()
#print(h)
n = list(range(1,20+1))
m = []
b = n[::]
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
else:
    print(m,n,b)