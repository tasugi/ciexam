def pban(objs):
    for i in range(15):
        for j in range(9):
            if (i,j) in objs:
                if(objs[i,j] in 'rl'):
                    print('o',end='')
                else:
                    print(objs[i,j],end='')
            else:
                if (j == 0 or j == 8):
                    print('|',end='')
                elif (i == 0):
                    print('-',end='')
                elif(i == 14):
                    print('.',end='')
                else:
                    print(' ',end='')
        print('')

if __name__ == '__main__':
    life = 5
    objs = {(0,4):'V',(14,4):'X'}
    score = 0
    while life > 0:
        pban(objs)
        newobjs = {}
        k  = input()
        newgame = 1
        if (k in 'jkl'):
            for (key,value) in objs.items():
                if (value == 'V'):
                    newobjs[key] = value
                elif(value == 'X'):
                    if(k == 'j' and key[1] > 0):
                        newobjs[(key[0],key[1]-1)] = value
                    elif(k == 'l' and key[1] < 8):
                        newobjs[(key[0],key[1]+1)] = value
                    else:
                        newobjs[key] = value
                elif(value == 'r'):
                    newgame = 0
                    if(key[0] == 13):
                        life += -1
                    elif(key[1] == 8):
                        newobjs[(key[0]+1,key[1]-1)] = 'l'
                    else:
                        newobjs[(key[0]+1,key[1]+1)] = 'r'
                elif(value == 'l'):
                    newgame = 0
                    if(key[0] == 13):
                        life += -1
                        newgame = 1
                    elif(key[1] == 0):
                        newobjs[(key[0]+1,key[1]+1)] = 'r'
                    else:
                        newobjs[(key[0]+1,key[1]-1)] = 'l'
                else:
                    print("This case may not occur.")
            if(newgame == 1):
                newobjs[1,5] = 'r'
                newgame = 0
            objs = newobjs
    print("Your score:",score)
