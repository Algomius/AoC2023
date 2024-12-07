depl = {
    "U" : (-1, 0),
    "D" : (1, 0),
    "L" : (0, -1),
    "R" : (0, 1)
}
#https://www.youtube.com/watch?v=bGWK76_e-LM
chiffreToDir = ["R", "D", "L", "U"]

pos = [0, 0]
perimetre = 0
points = []
f = open("input18.txt", "r")
for x in f:
    x = x[:-1]
    _, _, color = x.split()
    color = color[2:-1]
    direction = chiffreToDir[int(color[-1])]
    l = int(color[:-1], 16)

    perimetre += l
    d = depl[direction]
    deplX = pos[0]+ (int(l) * d[0])
    deplY = pos[1]+ (int(l) * d[1])
    pos = [deplX, deplY]
    points.append((deplX, deplY))

f.close()

# https://en.wikipedia.org/wiki/Shoelace_formula --> Other formulas
aire = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) //2 
i = aire - perimetre // 2 + 1 #https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Pick
print(i + perimetre)