
def L(source):
    lines = source.split('\n')
    vs = {}
    c = 0
    while c < len(lines):
        l = lines[c]
        s = l.split(' ')
        o = s[0]
        if(o == 'ADD'):
            if (s[1].isdecimal()):
                vs[s[2]] += int(s[1])
            else:
                vs[s[2]] += vs[s[1]]
            c+= 1
        elif(o=='PRN'):
            print(vs[s[1]],vs[s[2]])
            return
        elif(o=='SET'):
            vs[s[1]] = int(s[2])
            c += 1
        elif(o=='CMP'):
            if (s[1].isdecimal()):
                o1 = s[1]
            else:
                o1 = vs[s[1]]
            if (s[2].isdecimal()):
                o2 = s[2]
            else:
                o2 = vs[s[2]]
            if (o1 == o2):
                c += 2
            else:
                c += 1
        elif(o=='JMP'):
            c += int(s[1])


if __name__ == '__main__':
    with open('prog3.txt') as f:
        L(f.read())
