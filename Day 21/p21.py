from collections import deque

def parcours(m, pos, nbMouv):
    aVisiter = deque([(pos[0], pos[1], nbMouv)])
    lstValid = set()
    dejaVu ={(pos[0], pos[1])}
    while aVisiter:
        x, y, d= aVisiter.popleft()
        if d % 2 == 0:
            lstValid.add((x, y))
        if d == 0:
            continue

        for voisinX,voisinY  in [[x + 0,y + 1], [x+ 0,y-1], [x-1, y+0], [x+1, y+0]]:
            if 0 <= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                if m[voisinX][voisinY] != '#' :
                    if (voisinX, voisinY) not in dejaVu:
                        dejaVu.add((voisinX, voisinY))
                        aVisiter.append((voisinX, voisinY, d-1))

    return(len(lstValid))


m = []
indice = 0
f = open("input21.txt", "r")
for x in f:
    x  = x[:-1]
    if x.find('S') != -1:
        start = (indice, x.find('S'))
    m.append(list(x))
    indice += 1

print(parcours(m, start, 64))
