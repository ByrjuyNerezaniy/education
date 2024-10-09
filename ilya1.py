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
print(sorted(d))
# ________________________________________________________________________________________________#
num = input() 
splet = list(map(int, num.split()))
if max(splet) == len(splet) and len(set(splet)) == len(splet):
    print('OK')
else:
    print('BAD')





