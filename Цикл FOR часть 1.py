m = 'привет андрей'
count = 0
for i in m:
    if i == 'р':
        continue
    print(i)
else:
    print("Цикл завершен, количество букв р: ", count)
