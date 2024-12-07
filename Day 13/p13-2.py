mOri = []
mRenv = []

f = open("input13.txt", "r")
def getSym(m):
    for x in range(len(m)):
        nbDiff = 0
        indice = 0
        while 0 <= x-indice and x+indice+1 < len(m):
            for j in range(len(m[0])):
                if m[x-indice][j] != m[x+indice+1][j]:
                    nbDiff += 1
            indice += 1

        if nbDiff == 1:
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