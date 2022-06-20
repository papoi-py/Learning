
def count_list(par,par2 = False, count =0):  # переменная опр. только внутри функции, в неё помещается список
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par: #параметр по умолчанию вписывается последний
            count += 1
        return count

j = [9, 8, 7, 6]
dlina, tip = count_list (j, True) #аргумент - выводится кортеж, можно распаковать его на переменные
print(tip)

h = ['a', 'a', 'n']

print(count_list(h))

k = [9, 8, 7, 5, 7, 5]
len(j)