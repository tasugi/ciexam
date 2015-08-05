with open(prog1.txt) as f:
    L = f.read().split('\n')

for l in L:
    a = l.split(' ')
    print(a[1])
