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
# s = input()
# f = input()
# d1 = datetime.datetime.strptime(s, '%d.%m.%Y').date()
# d2 = datetime.datetime.strptime(f, '%d.%m.%Y').date()
# count = 0
# while d1 != d2:
#     d1 += datetime.timedelta(1)
#     count += 1
#print(f'в отпуске было {count + 1} рабочих дней')
#####################################################################
# f = input()
# d1 = datetime.datetime.strptime(f, '%d.%m.%Y').date()
# seasons = {
#     1: 'зима',
#     2: 'зима',
#     3: 'весна',
#     4: 'весна',
#     5: 'весна',
#     6: 'лето',
#     7: 'лето',
#     8: 'лето',
#     9: 'осень',
#     10: 'осень',
#     11: 'осень',
#     12: 'зима'
# }
# week_days = {
#     0: 'понедельник',
#     1: 'вторник',
#     2: 'среда',
#     3: 'четверг',
#     4: 'пятница',
#     5: 'суббота',
#     6: 'воскрсенье'
# }
# print(seasons.get(d1.month))
# print(week_days.get(d1.weekday()))
# if d1.weekday() <5:
#     print('будний')
# else:
#     print('выходной')
######################################################
s = input()
week_days = {
    0: 'понедельник',
    1: 'вторник',
    2: 'среда',
    3: 'четверг',
    4: 'пятница',
    5: 'суббота',
    6: 'воскресенье'
}
count_ = 0
sd = datetime.datetime.strptime(s, '%d.%m.%Y').date()
to_day = datetime.date.today()
fd = sd
td = to_day
while fd <= td:
    fd += datetime.timedelta(days = 1)
    if week_days.get(fd.weekday()) == 'воскресенье':
        count_ +=1
print(count_)
to_day -= sd
print(to_day)