mOri = []
mRenv = []

f = open("input13-temp.txt", "r")
def getSym(m):
    possible = []
    temp = ""
    for i in range(len(m)):
        if m[i] == temp:
            possible.append(i-1)
        temp = m[i]

    for x in possible:
        test = True
        indice = 0
        while 0 <= x-indice and x+indice+1 < len(m) and test:
            if m[x-indice] != m[x+indice+1]:
                test = False
            indice += 1

        if test:
            return x
    return -1

h = 0
v = 0
for x in f:
    x = x[:-1]
    if '.' in x or '#' in x:
        if not mOri:
            for _ in x:
                mRenv.append("")
        mOri.append(x)
        for i in range(len(x)):
            mRenv[len(mRenv)-1-i] += x[i]
    else:
        symV = getSym(mOri)
        if symV != -1:
            v += getSym(mOri) +1
        symH = getSym(mRenv)
        if symH != -1:
            h += len(mRenv) - symH -1
        mOri = []
        mRenv = []

if mOri:
    symV = getSym(mOri)
    if symV != -1:
        v += getSym(mOri) +1
    symH = getSym(mRenv)
    if symH != -1:
        h += len(mRenv) - symH -1
    print (v*100 + h)