f = open("program.txt")
t = f.read()

n = 0
for c in t:
    if (c == ';'):
        n += 1

print n
