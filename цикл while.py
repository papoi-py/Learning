x = ''
a = []
while len(x) < 5:
    y = input('Ввод данных: ')
    if not y == 'олень':
        print("не угадаль")
        continue
    if y == 'олень':
        print("лесгоу угадал")
        break
    x += y
else:
    print(x)


#while True:
#    x = int(input())
#    count = 0
#    foct = 1
 #   while count < x:
 #       count+=1
#        foct = foct * count
 #   else:
 #       print(foct)