# dict = {
#     'а': 1,
#     'б': 2,
#     'д': 3
# }
# w = 0
# word = ('аддаб')
# for i in range(len(word)):
#     letter = word[i]
#     w += dict[letter]
# print(w)
# dict = {
#     'а': 1,
#     'б': 2,
#     'д': 3
# }
# word = ('аддаб')
# w = 0
# for i in word:
#     w += dict[i]
# print(w)
# things = {
#     'палатка': 5500,
#     'спальный мешок': 2250,
#     'удочка': 1200,
#     'термос': 1000,
#     'бутерброды': 820,
#     'куртка': 600,
#     'фрукты': 500,
#     'бинокль': 400, 
#     'рубашка': 300,
#     'аптечка': 200, 
#     'компас': 100, 
#     'салфетки': 40,
#     'зажигалка': 20, 
#     'жвачка': 10
#     }
# weight = int(input()) * 1000
# result = []
# for thing, idx in things.items():
#     if weight > idx:
#         weight -= idx
#         result.append(thing)
# print(result)
# numbers = input().split()
# number = {}
# e = []
# for i in numbers:
#     if i not in e:
#         d = numbers.count(i)
#         number.update({i: d})
#         e.append(i)
# print(number)
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
d=[]
for i in emails:
    for values in emails.values():
        for numbers in range(len(values)):
            d.append(f'{values[numbers]}@{i}')
print(d)


