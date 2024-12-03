import datetime
import win10toast

file = open('example.txt', 'r', encoding='utf-8') # r -только чтение, a - добавить
today = datetime.datetime.now().date()
# today += datetime.timedelta(days=1)
today_str = datetime.datetime.strftime(today, '%Y-%m-%d')
while calling := file.readline():
    date, message = calling.split(':')
    if date == today_str:
        toaster = win10toast.ToastNotifier()
        toaster.show_toast('ALARM', message)
file.close()  