x = 'абвгдеёжзиклмнопрстуфхцчшщьъэюя'
y = input("Введите строку:\n")

for i in x:
    count = 0
    for j in y:
        if i == j:
            count += 1
    if count == 0:
        continue
    print("Букв ", i, "было ", count)