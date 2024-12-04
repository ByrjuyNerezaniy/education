import datetime
import os
import win10toast


def delete_diary(d, c):
    if d == '/c':
            file = open('днивник.txt', 'r+')
            file.truncate(0)
            file.close()
    if d == '/d':
            os.remove('C:\DonRobot\dmitrov_python\днивник.txt')


def write_diary():
    d= input(' Если хотите воспользоваться мной введите что-нибудь: ')
    print()
    s = bool(d)
    if s == True and d !='/c' and d!= '/d':
        file = open('diary.txt', 'a', encoding='utf-8')
        file.write(f'↓{datetime.datetime.now()}↓\n')
        file.write(f'{d} \n')
        file.close()
        print('запись совершена и дата добавленна')
    if d == '/rem':
        daata = input('введите дату когда вам напомнить')
        d1 = datetime.datetime.strptime(daata, '%d.%m.%Y').date()
        name = input('введите название уведомления: ')
        text = input('введитe текст уведомления: ')


def read_diary():
    file = open('diary.txt', 'r')
    h = file.readline().split()
    file.close()
    if datetime.datetime.now() > d1:
        if h[0][3:] == str(datetime.datetime.now().date()):
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(name, text)


def main():
    print('Здравствуте меня зовут Дарагой Днивник. Я ваш помощник чтобы не забыть информацию.')


main()