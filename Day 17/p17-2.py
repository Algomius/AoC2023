m = []
f = open("input17.txt", "r")
for x in f:
    x = x[:-1]
    m.append(list(map(int, list(x))))

aVisiter = [(0, 0, 0, 0, 0, 0)] # perte, posX, poY, depX, depY, nbDepl
dejaVu = set()
dejaVu.add((0, 0, 0, 0, 0))

while aVisiter:
    perte, posX, posY, depX, depY, nbDepl = aVisiter.pop()

    if posX == len(m)-1 and posY == len(m[0])-1 and nbDepl >= 4:
        print(perte)
        break

    if nbDepl < 10 and (depX, depY ) != (0, 0):
        voisinX = posX + depX
        voisinY = posY + depY
        if 0 <= voisinX < len(m) and 0 <= voisinY < len(m[0]):
            if (voisinX, voisinY, depX, depY, nbDepl + 1) not in dejaVu:
                aVisiter.append((perte + m[voisinX][voisinY], voisinX, voisinY, depX, depY, nbDepl + 1))
                dejaVu.add((voisinX, voisinY, depX, depY, nbDepl + 1))

    if nbDepl >= 4 or (depX, depY ) == (0, 0):
        for dirX, dirY in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            if (dirX, dirY) != (depX, depY) and (dirX, dirY) != (-depX, -depY):
                voisinX = posX + dirX
                voisinY = posY + dirY
                if 0 <= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                    if (voisinX, voisinY, dirX, dirY, 1) not in dejaVu:
                        aVisiter.append((perte + m[voisinX][voisinY], voisinX, voisinY, dirX, dirY, 1))
                        dejaVu.add((voisinX, voisinY, dirX, dirY, 1))

    aVisiter.sort(reverse=True)