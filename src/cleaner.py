from os import listdir, remove
from os.path import isfile, join, getctime
from time import time,sleep
def limpiar():
    files = [f for f in listdir('./generador/pdfs/') if isfile(join('./generador/pdfs/', f))]
    curr_time = time()
    exceed_time = 3600 #one hour
    for file in files:
        print(file)
        filetime=getctime('./generador/pdfs/'+file)
        if filetime+exceed_time<curr_time:
            remove('./generador/pdfs/'+file)

while True:
    limpiar()
    sleep(3600)#run every hour