l = [1] * 206

indice = 0
f = open("input4.txt", "r")
for x in f:
    y = x[:-1].split("|")
    gagnant = (y[0].split(":"))[1].split()
    carte = y[1].split()
    pts = 0
    for e in carte:
        if e in gagnant:
            pts += 1
    for _ in range(0, l[indice]):
        pts_temp = pts
        while pts_temp > 0:
            l[indice + pts_temp] += 1
            pts_temp -= 1
    indice += 1
print(sum(l))

