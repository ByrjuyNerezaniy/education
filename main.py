# a = [i for i in range(0, 10, 2)]
# print(a)

# a = [int(input()) for i in range]
# print(a)

# a=[int(input()) for i in range(5)]
# b = [i for i in a if i > 0]
# print(b)

# a=[int(input()) for i in range(5)]
# b= [i for i in a if i > sum(a)/len(a)]
# print(b)

countries = {"Россия": ["русский"],
             "Беларусь": ["белорусский", "русский"],
             "Бельгия": ["немецкий", "французский", "нидерландский"],
             "Вьетнам": ["вьетнамский"]}
a=[i for i in countries if len(countries[i]) > 1]             
print(a)