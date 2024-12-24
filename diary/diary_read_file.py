import datetime
import winsound
def allarm(): 
    for i in range(100, 2500, 100):
        winsound.Beep(i, 100)
        break
def dairy_read_file_cycle():    
    while True:
        file = open('diary.txt', 'r', encoding='utf-8')
        reading = file.readline()
        if '/a' in reading:
            allarm_time = reading.split(' : ')
            d1 = datetime.datetime.strptime(allarm_time, '%d.%m.%Y.%H.%M')
            if datetime.datetime.strptime(datetime.datetime.now(), '%d.%m.%Y.%H.%M') == d1:
                allarm()

