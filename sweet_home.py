while True:
    stroka = input().split(', ')
    print(stroka)
    slovar = {}
    for slovo in stroka:
        if slovo in slovar:
           slovar[slovo] = slovar.get(slovo) + 1
        else:
           slovar[slovo] = 1
    print(slovar)
