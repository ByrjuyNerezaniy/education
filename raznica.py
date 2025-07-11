arr = [4,2,1,3]
dbls = []
dfrnt = []
n= []
d= sorted(arr)
for i in range(len(d)):
    for a in range(i+1, len(d)):
        dbls.append([d[i], d[a]])
        dfrnt.append([d[a] - d[i]])
        f = set(dfrnt)
        n.append(dfrnt.index(min(f)))
res = []
for z in n:
    res.append(dbls[z])
print()