# words = input('введите предложение на русском или английском языке: ')
# r = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
# e = ['a', 'e', 'i', 'o', 'u']
# rg = 0
# rs = 0
# eg = 0
# es = 0
# for w in words:
#     if w in r:
#         rg += 1
#     if w not in r and w not in e:
#         rs += 1
#     if w in e:
#         eg += 1
#     if w not in r and w not in e:
#         es += 1
# words = input('введите предложение на русском или английском языке: ').lower()
# b = {}
# rgs = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
# rss = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
# egs = ['a', 'e', 'i', 'o', 'u']
# ess = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
# rg = 0
# rs = 0
# eg = 0
# es = 0
# for w in words:
#     if w in b:
#         b[w] += 1
#     else:
#         b[w] = 1
# for s in b:
#     if s in rgs:
#         rg += 1
#     if s in rss:
#         rs += 1
#     if s in egs:
#         eg += 1
#     if s in ess:
#         es += 1
words = input('введите предложение на русском или английском языке: ')
b = {}
r = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
e = ['a', 'e', 'i', 'o', 'u']
rg = 0
rs = 0
eg = 0
es = 0
l = True
for w in words:
    if w in b:
        b[w] += 1
    else:
        b[w] = 1
for w in words:
    if w in r:
        l = True
    if w in e:
        l = False
for i in b:
    