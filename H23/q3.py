def makeDic(s):
    d = {}
    for i in range(len(s)-5):
        if (s[i:i+6] in d):
            pass
        else:
            d[s[i:i+6]] = (str(i)).zfill(3)
    return d

if __name__ == '__main__':
    with open("data/s1.txt") as f:
        s = f.read()
    d = makeDic(s)
    n = len(d)
    print(n)
