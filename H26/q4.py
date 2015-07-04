import math
l = 3
ss = 10 * 5 * math.sqrt(3) /2

n = int(input('-->'))
s = ss
for i in range(n):
    ss = ss / (3**2)
    s = s + ss * l
    l = 4 * l

print('K({0}) = {1}'.format(n,s))
