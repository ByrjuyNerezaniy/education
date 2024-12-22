import datetime
import os
import diary_read_file
print('Здравствуте меня зовут Дарагой Днивник. Я ваш помощник чтобы не забыть информацию.')
text_user = ''
diary_read_file.dairy_read_file_cycle()
#основанеие_____________________________________________________________________
def main():
    while True:
        commands()
#запись_______________________________________________________________________
def write():
        try:
            text_user = input()
            file = open('diary.txt', 'a', encoding='utf-8')
            file.write(f'{datetime.datetime.now()} : {text_user} \n')
            file.close()
        except FileNotFoundError:
            print('Файл не существует.\n Чтобы создать его введите "/w" ')

#чтение_______________________________________________________________________
def read():
        try:
            file = open('diary.txt', 'r', encoding='utf-8')
            read_variable = file.read()
            file.close()
            print(read_variable)
        except FileNotFoundError:
            print('Файл не существует.\nЧтобы создать его введите "/w" ')

#удаление_____________________________________________________________________
def delite():
    try:
        os.remove('C:\DonRobot\dmitrov_python\diary.txt')
    except FileNotFoundError:
        print('Файл не существует.\n Чтобы создать его введите "/w" ')
#очистка______________________________________________________________________
def clear():
    try:
        file = open('diary.txt', 'r+')
        file.truncate(0)
        file.close()
    except FileNotFoundError:
        print( 'Файл не существует.\n Чтобы создать его введите "/w" ')
#будильник_____________________________________________________________________
def allarm_time():
    date_time = input('введите дату и время: ')
    file = open('diary.txt', 'a', encoding='utf-8')
    file.write(f'/rem : {date_time}')
    file.close()
#команды_______________________________________________________________________
def commands():
    texxt = input('Если хотите воспользоваться мной введите что-нибудь: ')
    match texxt:
        case '/w': write()
        case '/r': read()
        case '/c': clear()
        case '/d': delite()
        case '/a': allarm_time
        case _: print('команда не действительна')
if __name__ == '__main__':
    main()