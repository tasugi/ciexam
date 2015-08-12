def pban(v,g,m,t_all):
    for r in range(15):
        for c in range(9):
            if (g == [r,c]):
                print('X',end='')
            elif(v == [r,c]):
                print('V',end='')
            elif(m == [r,c]):
                print('o',end='')
            elif([r,c] in t_all):
                print('e',end='')
            elif(c in [0,8]):
                print('|',end='')
            elif(r in [0,14]):
                print('.',end='')
            else:
                print(' ',end='')
        print('')


if __name__ == '__main__':
    score = 0
    life = 5
    stock = 2
    vpos = [0,4]
    gan = [14,4]
    mato = {'pos':[-1,-1],'muki':0}
    tama_all = []
    while life > 0:
        pban(vpos,gan,mato['pos'],tama_all)
        key = input()
        if(key in 'ijkl'):
            if (mato['muki'] == 0):
                mato['pos'] = vpos
                mato['muki'] = 1
                stock = 2
            if (key=='i' and stock > 0):
                stock -= 1
                tama_all.append(gan)
            mato['pos'] = [mato['pos'][0]+1,mato['pos'][1]+mato['muki']]
            if (mato['pos'][1] == 0 or mato['pos'][1] == 8):
                mato['muki'] = - mato['muki']
            if (mato['pos'][0] == 14):
                life -= 1
                mato = {'pos':[-1,-1],'muki':0}
            ntama_all = []
            for t in tama_all:
                if (mato['pos'] == [t[0]-1,t[1]]):
                    mato = {'pos':[-1,-1],'muki':0}
                    score += 1
                elif (t[0] == 1):
                    pass
                else:
                    ntama_all.append([t[0]-1,t[1]])
            tama_all = ntama_all
    print("Your score:",score)
