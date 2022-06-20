import os
import time

while True:
    sayt = input("Введите адрес сайта\n")
    if sayt == 'end':
        break
    # метод os.system
    #в круглых скобках подаётся аргумент
    # нужно подать ключевое слово 'start https://youtube.com'
    if 'https://' in sayt:
        os.system("start "    + sayt)
        print("if")
    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
        #после команды start обязательно нужно поставить пробел, иначе программа будет выдавать ошибку
        print("elif")
    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)
        print("else")

    print(sayt)