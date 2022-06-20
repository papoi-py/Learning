import os
import time
spisok = []
#('C:\\Users\\paPoi\\Desktop\\практика', ['папка1', 'папка2'], ['файл1.txt', 'файл2.txt'])
for adres, dirs, files in os.walk('C:\\Users\paPoi\Desktop\пример'):
    for file in files:
        full = os.path.join (adres, file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)#поставить слеш между строк, чтобы адрес работа
print(spisok)