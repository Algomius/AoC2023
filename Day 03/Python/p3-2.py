def getNum(l, x, y):
    while y >= 0 and "0" <= l[x][y] <= "9":
        y -= 1
    y += 1
    debut = y
    num = 0
    while y < len(l[x]) and "0" <= l[x][y] <= "9":
        num *= 10
        num += int(l[x][y])
        y += 1
    return num, debut


l = []
f = open("input3.txt", "r")
for x in f:
    l.append(x[:-1])

somme = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "*":
            n = []
            dejaVu = []
            for k in range(-1,2):
                for m in range(-1,2):
                    voisinX = i + k
                    voisinY = j + m
                    if 0 <= voisinX < len(l) and 0 <= voisinY < len(l[i]):
                        if "0" <= l[voisinX][voisinY] <= "9":
                            num, col = getNum(l, voisinX, voisinY)
                            if (voisinX,col) not in dejaVu:
                                n.append(num)
                                dejaVu.append((voisinX, col))

            if len(n) == 2:
                somme += (n[0] * n[1]) 

print(somme)