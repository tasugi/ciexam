from q3 import makeDic

def asshuku(s):
    d = makeDic(s)
    j = 0
    c = ''
    while j < len(s) - 5:
        if d[s[j:j+6]] == (str(j)).zfill(3):
            c += s[j]
            j += 1
        else:
            c += d[s[j:j+6]]
            j += 6
    c += s[j:]
    return c

if __name__ == '__main__':
    with open("data/s1.txt") as f:
        s = f.read()
    s1 = asshuku(s)
    print("s1.txt")
    print("len:{0}. last10:{1}".format(len(s1), s1[-10:]))

    with open("data/s2.txt") as f:
        s = f.read()
    s2 = asshuku(s)
    print("s2.txt")
    print("len:{0}. last10:{1}".format(len(s2), s2[-10:]))
