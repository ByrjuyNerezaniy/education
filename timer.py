import datetime
import time
# monthes = {
#     1: 'января',
#     2: 'февраля',
#     3: 'марта',
#     4: 'апреля',
#     5: 'майа',
#     6: 'июня',
#     7: 'июля',
#     8: 'августа',
#     9: 'сентября',
#     10: 'октября',
#     11: 'ноября',
#     12:  'декабря'
# }
# ti = datetime.datetime.now()
# print(f'Сегодня {ti.day} {monthes.get(ti.month)} {ti.year} года')
####################################################################
# t1 = int(input())
# ti = datetime.datetime.now()
# print(ti)
# time.sleep(t1)
# print(ti)
####################################################################
s = int(input)
f = int(input)
d1 = datetime.datetime.strptime(s, '%d.%m.%Y').date
d2 = datetime.datetime.strptime(f, '%d.%m.%Y').date
while d1 != d2:
    print(d2.day -= 1)