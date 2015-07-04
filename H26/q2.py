import math

d = abs(float(input('Please set d:')))

ans = 0
for p in range(math.ceil(10/d)+1):
    for q in range(math.ceil(10/d)+1):
        if ( (d*p -5 )**2 + (d*q -5)**2 <= 5**2):
            ans += 1

n = math.floor(10.0/abs(d)) + 1
a = ans / n**2 /4

print(a)
