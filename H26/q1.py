import math

d = float(input('Please set d:'))

n = math.floor(10.0/abs(d)) + 1

print('A({0},R_0) = {1}'.format(d,n*n))
