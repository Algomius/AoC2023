depl = {
    "U" : (-1, 0),
    "D" : (1, 0),
    "L" : (0, -1),
    "R" : (0, 1)
}


def diffusion(m, pos):
    aVisiter = [pos]
    while aVisiter:
        n = aVisiter.pop()
        m[n[0]][n[1]] = "S"
        for e in depl.keys():
            deplX = n[0]+ depl[e][0]
            deplY = n[1]+ depl[e][1]
            if 0<= deplX < len(m) and 0 <= deplY < len(m[0]):
                if m[deplX][deplY] == "." and [deplX, deplY] not in aVisiter:
                    aVisiter.append([deplX, deplY])


pos = [0, 0]
minX = 0
maxX = 0
minY = 0
maxY = 0


f = open("input18.txt", "r")
for x in f:
    x = x[:-1]
    direction, l, color = x.split()
    d = depl[direction]
    deplX = pos[0]+ (int(l) * d[0])
    deplY = pos[1]+ (int(l) * d[1])
    pos = [deplX, deplY]
    minX=min(minX, deplX)
    maxX=max(maxX, deplX)
    minY=min(minY, deplY)
    maxY=max(maxY, deplY)

f.close()


m = [['.' for _ in range(maxY-minY+1)] for _ in range(maxX-minX+1)]
print(minX, " - ",  maxX, " - ", minY, " - ", maxY)

pos = [-minX, -minY]
f = open("input18.txt", "r")
for x in f:
    x = x[:-1]
    direction, l, color = x.split()
    d = depl[direction]
    l = int(l)
    while l > 0:
        deplX = pos[0]+ d[0]
        deplY = pos[1]+ d[1]
        m[deplX][deplY] = "#"
        pos = [deplX, deplY]
        l -= 1

diffusion(m, [0, len(m[0]) - 1])
diffusion(m, [0, 0])
diffusion(m, [len(m)-1, 0])
diffusion(m, [len(m)-1, len(m[0]) -1])

nb = 0
for e in m:
    for i in e:
        if i != "S":
            nb += 1

print(nb)




for e in m:
    print(e)