pente = {
    ">" : [(0, 1)],
    "<" : [(0, -1)],
    "v" : [(1, 0)],
    "^" : [(-1, 0)],
    "." : [(0, 1), (1, 0),(-1, 0), (0, -1)]
}
def longCheminIter(m, pos, end):
    maxDist = -1
    aVisiter = [((pos[0], pos[1]), 0, [])]
    while aVisiter:
        position, longueur, visite = aVisiter.pop()
        if position == end:
            maxDist = max(maxDist, longueur)
        else:
            for v in pente[m[position[0]][position[1]]]:
                voisinX = position[0] + v[0]
                voisinY = position[1] + v[1]
                if 0<= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                    if m[voisinX][voisinY] != '#' and (voisinX, voisinY) not in visite:
                        aVisiter.append(((voisinX, voisinY), longueur+1, visite + [position]))
    return maxDist

def longChemin(m, pos, end, longueur=0, visite=[]):
    if pos == end:
        return longueur
    else:
        visite.append(pos)
        if m[pos[0]][pos[1]] == '.':
            dist = -1
            for v in [[0, 1], [1, 0],[-1, 0], [0, -1]]:
                voisinX = pos[0] + v[0]
                voisinY = pos[1] + v[1]
                if 0<= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                    if m[voisinX][voisinY] != '#' and (voisinX, voisinY) not in visite:
                        d = longChemin(m, (voisinX, voisinY), end, longueur+1, visite[:])
                        dist = max(dist, d)
            return dist

        else:
            voisinX = pos[0] + pente[m[pos[0]][pos[1]]][0]
            voisinY = pos[1] + pente[m[pos[0]][pos[1]]][1]
            if 0<= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                if m[voisinX][voisinY] != '#' and (voisinX, voisinY) not in visite:
                    return longChemin(m, (voisinX, voisinY), end, longueur+1, visite[:])
                
            return -1
        



m = []
f = open("input23.txt", "r")
for x in f:
    x  = x[:-1]
    m.append(list(x))

start = (0, m[0].index("."))
end = (len(m)-1, m[len(m)-1].index("."))

print(longCheminIter(m, start, end))