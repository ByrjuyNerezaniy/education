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
things = {
    'палатка': 5500,
    'спальный мешок': 2250,
    'удочка': 1200,
    'термос': 1000,
    'бутерброды': 820,
    'куртка': 600,
    'фрукты': 500,
    'бинокль': 400, 
    'рубашка': 300,
    'аптечка': 200, 
    'компас': 100, 
    'салфетки': 40,
    'зажигалка': 20, 
    'жвачка': 10
    }
weight = int(input()) * 1000
result = []
for thing, idx in things.items():
    if weight > idx:
        weight -= idx
        result.append(thing)
print(result)