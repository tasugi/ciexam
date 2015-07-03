f = open("program.txt")
l = f.readlines()

for i,ll in enumerate(l):
    print(i,ll.strip('\n'))
