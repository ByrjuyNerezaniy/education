t1 = input()
t2 = input()
t3 = input()
if t1 == t2 == t3:
    print('равносторонрий')

if t1 != t2 != t3:
    print('разносторонний')

if t1 == t2 != t3:
    print('равнобедренный')
if t1 != t2 == t3:
    print('равнобедренный')
if t1 == t3 != t2:
    print('равнобедренный')
