def s(s1,s2):
    l = max(len(s1),len(s2))
    ss1 = s1 + ' ' * (l - len(s1))
    ss2 = s2 + ' ' * (l - len(s2))
    c = 0
    for i in range(l):
        if (ss1[i] != ss2[i]):
            c += 1
    return c

f = open("program.txt")
l = f.read().split('\n')
ll = []
for lll in l:
    if (len(lll) >=20 and lll not in ll):
        ll.append(lll)
row = len(ll)
for i in range(row):
    for j in range(i+1,row):
        if (s(ll[i],ll[j]) < 5 and s(ll[i],ll[j]) != 0):
            print(ll[i],ll[j],sep=',')
