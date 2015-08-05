
def L(source):
    lines = source.split('\n')
    vs = {}
    for l in lines:
        s = l.split(' ')
        o = s[0]
        if(o == 'ADD'):
            if (s[1].isdecimal()):
                vs[s[2]] += int(s[1])
            else:
                vs[s[2]] += vs[s[1]]
        elif(o=='PRN'):
            print(vs[s[1]],vs[s[2]])
            return
        elif(o=='SET'):
            vs[s[1]] = int(s[2])

if __name__ == '__main__':
    with open('prog2.txt') as f:
        L(f.read())
