#четность числа
# a = int(input())
# if a % 2 == 0:
#     print(True)


# a = int(input())
# print(a % 2 == 0)
##################################################
#A : B = положительное число
# a = int(input())
# b = int(input())
# if a/b < 0:
#     print(False)
# else:
#     print(True)


# a = int(input())
# b = int(input())
# print(a/b < 0)
#########################################################
# # a = положтельное число
# a = int(input())
# if a < 0:
#     print(False)
# else:
#     print(True)


# a = int(input())
# print(a < 0)
slovo1 = input()
slovo2 = input()
d = True
if len(slovo1) != len(slovo2):
    print(False)
else:
    for i in range(len(slovo1)):
        if slovo2[i] not in slovo1:
            d =False
        if slovo1[i] not in slovo2:
            d =False
    print(d)
















