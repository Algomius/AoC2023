def fixeBloc(v, n, sx, sy, sz, ex, ey, ez):
    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            for k in range(sz, ez+1):
                v[i][j][k] = n 

def descente(v, n, sx, sy, sz, ex, ey, ez):
    d = 0
    n = []
    testSol = False
    while not testSol and n == []:
        d += 1
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                for k in range(sz, ez+1):
                    if k-d >= 0: 
                        if v[i][j][k-d] != -1 and v[i][j][k-d] not in n:
                            n.append(v[i][j][k-d])
                    else:
                        testSol = True 
        

    return d-1, n

l = []
maxX = 0
maxY = 0
maxZ = 0
f = open("input22.txt", "r")
for x in f:
    x  = x[:-1]
    start,end = x.split("~")
    s = list(map(int, start.split(",") ))
    maxX = max(maxX, s[0])
    maxY = max(maxY, s[1])
    maxZ = max(maxZ, s[2])
    s.reverse()
    e = list(map(int, end.split(",")))
    maxX = max(maxX, e[0])
    maxY = max(maxY, e[1])
    maxZ = max(maxZ, e[2])
    e.reverse()
    if e < s:
        l.append((e,s))
    else:
        l.append((s,e))

l.sort()
v = [[ [-1 for _ in range(maxZ+1)] for _ in range(maxY+1)] for row in range(maxX+1)]
pred = [[] for _ in range(len(l))]


for i in range(len(l)):
    s, e = l[i]
    sz, sy, sx = s
    ez, ey, ex = e
    d, n = descente(v, i, sx, sy, sz, ex, ey, ez)
    fixeBloc(v, i, sx, sy, sz-d, ex, ey, ez-d)
    pred[i] += n

nbDesintegre = 0
for i in range(len(pred)):
    tstDesintegre = True
    for x in pred:
        if i in x and len(x) == 1:
           tstDesintegre = False

    if tstDesintegre:
         nbDesintegre += 1

print(nbDesintegre)
