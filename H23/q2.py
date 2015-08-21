def count(s):
    count = 0
    for c in s:
        if (c.isdecimal()):
            count += 1
    count = count/3
    return int(count)

with open("data/c1.txt") as f:
    s = f.read()
c = count(s)
print("c1.txt:",c)

with open("data/c2.txt") as f:
    s = f.read()
c = count(s)
print("c2.txt:",c)
