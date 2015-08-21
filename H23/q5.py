
def tenkai(c):
    s = ''
    j = 0
    while j < len(c):
        if not c[j].isdecimal():
            s += c[j]
            j += 1
        else:
            num = int(c[j:j+3])
            j += 3
            for i in range(6):
                s += s[num+i]
    return s

if __name__ == '__main__':
    with open("data/c1.txt") as f:
        c = f.read()
    s = tenkai(c)
    print("c1.txt")
    print("len:{0} last10:{1}".format(len(s), s[-10:]))

    with open("data/c2.txt") as f:
        c = f.read()
    s = tenkai(c)
    print("c2.txt")
    print("len:{0} last10:{1}".format(len(s), s[-10:]))
