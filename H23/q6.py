from q4 import asshuku
from q5 import tenkai

def asshuku2(ls):
    n = len(ls)
    lc = ''
    i = 0
    while 1000 * i < n:
        s = ls[1000*i:min(1000*(i+1),n)]
        c = asshuku(s)
        lc += c
        i += 1
    return lc

def tenkai2(lc):
    s = ''
    j = 0
    while j < len(lc):
        if not lc[j].isdecimal():
            s += lc[j]
            j += 1
        else:
            num = int(lc[j:j+3])
            j += 3
            d = (len(s) // 1000) * 1000
            for i in range(6):
                s += s[num+i+d]
    return s

if __name__ == '__main__':
    with open("data/s3.txt") as f:
        ls = f.read()
    lc = asshuku2(ls)
    nls = tenkai2(lc)
    print("Result:",ls == nls)
