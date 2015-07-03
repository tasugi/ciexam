f = open("program.txt")
l = f.read().split('\n')

r = []
for i,ll in enumerate(l):
    if( (ll in l[:i] or ll in l[i+1:]) and ll not in r):
        r.append(ll)

print(len(r))
for rr in r:
    print(rr)
