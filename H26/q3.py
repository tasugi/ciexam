import math
l = 3
ss = 10 * 5 * math.sqrt(3) /2

s = ss
for i in range(2):
    ss = ss / (3**2)
    s = s + ss * l
    l = 4 * l

print('K(2) =',s)
