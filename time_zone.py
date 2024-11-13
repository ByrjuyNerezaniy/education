import datetime
import pytz
# start_place = input()
# finish_place = input()
# d1 = datetime.datetime.strptime(start_place, '%d.%m.%Y')
# d2 = datetime.datetime.strptime(finish_place, '%d.%m.%Y')
# stt = input('введите время начала пути: ')
# fit = input('введите время конца пути: ')
allt = int(input('введите время пути: '))
# spt = pytz.timezone(stt)
# fpt = pytz.timezone(fit)

s = datetime.datetime(2024,11,14,10,00,00)
f = datetime.timedelta(hours=allt)
l = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
d = s.date() - l.date()
# d += d2 - d1
print(d)
 #+ (datetime.time(pytz.timezone(start_place)) - datetime.time(pytz.timezone(finish_place)))




