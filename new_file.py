f = input('какую единицу измерения градусов вы хотите преобразовать: ')
f1 = input('в какую единицу измерения градусов вы хотите преобразовать: ')
number = int(input('какое число вы хотите преобразовать: '))
slovar={
    'ck': number + 273,
    'kc': number - 273,
    'cf': 1.8 * number + 32,
    'fc': (number - 32) / 1.8,
    'kf': ((number-273.15)*9)/5+32,
    'fk': (number + 459.67) * 0.6, 
}
if f == 'фаренгейт' and f1 =='цельсий':
    print(slovar.get('fc'))
if f == 'цельсий' and f1 =='фаренгейт':
    print(slovar.get('cf'))
if f == 'фаренгейт' and f1 =='кальвин':
    print(slovar.get('fk'))
if f == 'кальвин' and f1 =='фаренгейт':
    print(slovar.get('kf'))
if f == 'цельсий' and f1 =='кальвин':
    print(slovar.get('ck'))
if f == 'кальвин' and f1 =='цельсий':
    print(slovar.get('kc'))




