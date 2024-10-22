slovo1 = input().lower()
slovo2 = input().lower()
h = ''
k = ''
for d in slovo1:
    if d.isalpha():
        h += d
for m in slovo2:
    if m.isalpha():
        k += m
d = True
if len(h) != len(k):
    d =False
else:
    for i in range(len(h)):
        if k[i] not in h:
            d =False

        if h[i] not in k:
            d =False
print(d)