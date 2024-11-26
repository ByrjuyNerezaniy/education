import datetime
import os
print('Здравствуте меня зовут Дарагой Днивник. Я ваш помощник чтобы не забыть информацию.')
while True:
    d= input(' Если хотите воспользоваться мной введите что-нибудь: ')
    s = bool(d)
    if s == True and d !='/c' and d!= '/d':
        file = open('днивник.txt', 'a', encoding='utf-8')
        file.write(f'↓{datetime.datetime.now()}↓\n')
        file.write(f'{d} \n')
        file.close()
        print('запись совершена и дата добавленна')
    if d == '/c':
        file = open('днивник.txt', 'r+')
        file.truncate(0)
        file.close()
    if d == '/d':
        os.remove('C:\DonRobot\dmitrov_python\днивник.txt')



