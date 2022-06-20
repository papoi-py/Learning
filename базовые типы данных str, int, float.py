#типы данных
a = 'string' + '12345'
print(a)
x = float(input('Введите число '))
y = float(input('Введите число '))
r = x + y
#print("Резульат: " + r) - ERROR
print("Резульат: " + str(r)) #-GOOD
print(1 + r)
# input передаёт значение введённое пользователем в виде строки

#float(5)
#print(float)