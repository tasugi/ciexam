f = open("program.txt")
l = f.readlines()

p = ''
c = 1
for ll in l:
    if (p == ll and c == 1):
        print(p)
        c += 1
    elif(p != ll):
        c = 1
    p = ll
