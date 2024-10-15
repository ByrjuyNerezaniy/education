glasnie = ['a', 'e', 'i', 'o', 'u']
soglasnie = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')
letter = input('введите букву латинского алфавита: ')
letter.lower
if letter in glasnie:
    print('это гласная буква')
elif letter == 'y':
    print('эта буква может быть и гласной и согласной')
elif letter in soglasnie:
    print('это согласная буква')


