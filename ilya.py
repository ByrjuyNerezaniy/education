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
    # 'а': 1,
    # 'б': 2,
    # 'д': 3
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
# workers = {
#     'name1': 'wowowo@gmail.com',
#     'name2': 'xoxoxo@gmail.com',
#     'name3': 'dododo@gmail.com',
# }
# while True:
#     name = input('введите ваше имя: ')
#     if name in workers:
#         print(f'вот ваша почта {workers.get(name)}! Добро пожаловать')
#     else:
#         d = input('Добро пожаловать в коллектив! Введите свою почту: ')
#         workers.update({ name: d})
workers = {
    1: ['name1','wowowo@gmail.com'],
    2: ['name2','xoxoxo@gmail.com' ],
    3: ['name3','dododo@gmail.com'],
}
while True:
    email = ()
    name = input('введите ваше имя: ')
    for i in workers:
        d = workers.get(i)[0]
        if name == d:
            print(f'Добро пожаловать! Ваша почта {workers.get(i)[1]}')
        else:
            email = input(f'Добро пожаловать в коллетктив {name}! Введите вашу почту: ')
        workers.update({name: email})








