x = 'a'

if x == 0:
    x = 1
    print('x был равен нулю')
elif type(x) == type(5) or type(x) == type(5.5):
    print('x - допустимое значение')

else:
    print('x - недопустимый тип данных')
    x = 1

print(100/x)