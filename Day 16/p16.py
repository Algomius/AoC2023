d = {
    "N" : (-1, 0),
    "S" : (+1, 0),
    "E" : (0, +1),
    "W" : (0, -1)
}

n = {
    "N" : {"." : ["N"], "|" : ["N"], "-" : ["E", "W"], "/" : ["E"], "\\" : ["W"]},
    "S" : {"." : ["S"], "|" : ["S"], "-" : ["E", "W"], "/" : ["W"], "\\" : ["E"]},
    "E" : {"." : ["E"], "|" : ["N", "S"], "-" : ["E"], "/" : ["N"], "\\" : ["S"]},
    "W" : {"." : ["W"], "|" : ["N", "S"], "-" : ["W"], "/" : ["S"], "\\" : ["N"]}
}

m = []
f = open("input16.txt", "r")
for x in f:
    x = x[:-1]
    m.append(list(x))


deplSave = [[[] for _ in range(len(m[0]))] for _ in range(len(m))]
dejaVu = []
aVisiter = [(0, 0, "E")]

while aVisiter:
    x, y, direction = aVisiter.pop()
    deplSave[x][y].append(direction)
    if (x, y) not in dejaVu:
        dejaVu.append((x,y))
    nouvelleDir = n[direction][m[x][y]]
    for e in nouvelleDir:
        depl = d[e]
        if 0 <= x+depl[0] < len(m) and 0 <= y+depl[1] < len(m[0]):
            if e not in deplSave[x+depl[0]][y+depl[1]]:
                aVisiter.append((x+depl[0], y+depl[1], e))

print(len(dejaVu))
