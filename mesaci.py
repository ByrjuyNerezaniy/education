mesac = input('введите название мясяца: ').lower()
daysss =  { 'январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь'}
dayss = {'апрель', 'июнь', 'сентябрь', 'ноябрь'}
if mesac in daysss:
    print(31)
elif mesac in dayss:
    print(31)
if mesac == 'февраль':
    print('может быть как 29 так и 28 дней')
if mesac not in dayss and mesac not in daysss:
    if mesac != 'февраль':
        print('такого месяца нет')





