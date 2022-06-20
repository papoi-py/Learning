import os
import time
spisok = []
for adress, dirs, files in os.walk("C:\\Users\paPoi\Desktop\пример"):
    for file in files:
        if ".txt" in file:
            spisok.append (os.path.join (adress, file))

print(spisok)