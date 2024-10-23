import random
num = 0
spisok = []
for i in range(10000000):
    num += random.randint(0, 10000000)
    spisok.append(num)
with open('test.txt', 'w') as file:
    file.write(' '.join(map(str, spisok)))










