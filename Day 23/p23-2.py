def parcoursProfondeur(g, pos, end, dejaVu= []):
    if pos == end:
        return 0
    
    maxDist = -float("inf")

    for x in g[pos].keys():
        if x not in dejaVu and x != pos:
            maxDist = max(maxDist, parcoursProfondeur(g, x, end, dejaVu + [pos]) + g[pos][x])
                
    return maxDist


def embranchement(m):
    emb = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != "#":
                nbVoisin = 0
                for v in [[0, 1], [1, 0],[-1, 0], [0, -1]]:
                    voisinX = i + v[0]
                    voisinY = j + v[1]
                    if 0<= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                        if m[voisinX][voisinY] != '#':
                            nbVoisin += 1
                if nbVoisin > 2:
                    emb.append((i, j))
    return emb

m = []
f = open("input23.txt", "r")
for x in f:
    x  = x[:-1]
    m.append(list(x))

start = (0, m[0].index("."))
end = (len(m)-1, m[len(m)-1].index("."))

emb = embranchement(m) 
emb = [start] + emb + [end]

graphSimplifie = {x: {} for x in emb}

for oriX, oriY in graphSimplifie:   
    aVisiter = [(0, oriX, oriY)]
    dejaVu = [(oriX, oriY)]

    while aVisiter:
        dist, x, y = aVisiter.pop()
        
        if dist != 0 and (x, y) in emb:
            graphSimplifie[(oriX, oriY)][(x, y)] = dist
        else:
            for v in [[0, 1], [1, 0],[-1, 0], [0, -1]]:
                voisinX = x + v[0]
                voisinY = y + v[1]
                if 0<= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                    if m[voisinX][voisinY] != '#' and (voisinX, voisinY) not in dejaVu:
                        aVisiter.append((dist + 1, voisinX, voisinY))
                        dejaVu.append((voisinX, voisinY))

print(parcoursProfondeur(graphSimplifie, start, end))
