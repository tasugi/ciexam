def s(s1,s2):
    t = {}
    for i in range(len(s1)+1):
        t[i,0] = i
    for i in range(len(s2)+1):
        t[0,i] = i
    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            if (s1[i-1]  == s2[j-1]):
                d = 0
            else:
                d = 1
            t[i,j] = min(t[i,j-1]+1,t[i-1,j]+1,t[i-1,j-1]+d)
    return t[len(s1),len(s2)]

f = open("program.txt")
l = f.read().split('\n')
ll = []
for lll in l:
    if (len(lll) >=0 and lll not in ll):
        ll.append(lll)
row = len(ll)
for i in range(row):
    for j in range(i+1,row):
        if (s(ll[i],ll[j]) < 5 and s(ll[i],ll[j]) != 0):
            print(ll[i],ll[j],sep=',')
