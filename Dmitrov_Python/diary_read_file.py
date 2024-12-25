import datetime
import winsound
import time
# будильник_________________________________
def allarm(): 
    print('chiuaua')
    winsound.Beep(800, 3000)

# переменные_________________________________
def comands():
    file = open('diary.txt', 'r', encoding='utf-8')
    read_text = file.readlines()
    file.close()
    return read_text
    
# цикл чтения_________________________________

def dairy_read_file_cycle(count=0):    
    file = open('diary.txt', 'r', encoding='utf-8')
    strings = comands()
    while count != len(strings):
        reading = file.readline()
        # print(reading)
        count = count + 1 
        # print('/a' in reading, reading)
        if '/a' in reading:
            allarm_time = reading.split(' : ')
            # print(allarm_time[1][:16])
            d1 = datetime.datetime.strptime(allarm_time[1][:16], '%d.%m.%Y %H.%M')
            d = datetime.datetime.strftime(datetime.datetime.now(), '%d.%m.%Y %H.%M')
            d2 = datetime.datetime.strptime(d, '%d.%m.%Y %H.%M')
            print(f'{d1} = {d2} {d1==d2}')
            # print(d2)
            if  d2 == d1:
                allarm()
    file.close()
    




def allarm_main():
    strings = comands()
    while True:
        if len(strings) > 0:
            dairy_read_file_cycle()
        time.sleep(20)
# allarm_main()

if __name__ == '__main__':
    allarm_main()