import datetime
import winsound
import time
# будильник_________________________________
def allarm(): 
    for i in range(100, 2500, 100):
        winsound.Beep(i, 100)
        break
# переменные_________________________________
file = open('diary.txt', 'r', encoding='utf-8')
read_text = file.readlines()
file.close()
# цикл чтения_________________________________
def dairy_read_file_cycle(count=0):    
    file = open('diary.txt', 'r', encoding='utf-8')
    while count != len(read_text):
        reading = file.readline()
        # print(reading)
        count = count + 1 
        # print('/a' in reading, reading)
        if '/a' in reading:
            allarm_time = reading.split(' : ')
            print(allarm_time[1][:16])
            d1 = datetime.datetime.strptime(allarm_time[1][:16], '%d.%m.%Y %H.%M')
            d = datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y %H.%M')
            if datetime.datetime.strptime(d, '%d.%m.%Y %H.%M') == d1:
                allarm()
    file.close()




def allarm_main():
    while True:
        if len(read_text) > 0:
            dairy_read_file_cycle()
        time.sleep(60)
allarm_main()
