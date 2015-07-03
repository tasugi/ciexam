
def myj(l,r):
    for rr in r:
        if l in rr:
            return False
    return True

f = open("program.txt")
l = f.read().split('\n')
r = []
for i in range(len(l)):
    for j in range(i+1,len(l)):
        d = 0
        while j+d < len(l) and l[i+d] == l[j+d]:
            d += 1
        t = '\n'.join(l[i:i+d])
        if d >=4 and myj(t,r):
            print(t)
            print('')
            r.append(t)
