l = []
f = open("input3.txt", "r")
for x in f:
    l.append(x[:-1])

somme = 0
for i in range(len(l)):
    num = 0
    prendre = False
    for j in range(len(l[i])):
        if "0" <= l[i][j] <= "9":
            num *= 10
            num += int(l[i][j])
            if not prendre:
                for k in range(-1,2):
                    for m in range(-1,2):
                        voisinX = i + k
                        voisinY = j + m
                        if 0 <= voisinX < len(l) and 0 <= voisinY < len(l[i]):
                            if ("0" > l[voisinX][voisinY] or l[voisinX][voisinY] > "9") and l[voisinX][voisinY] != ".":
                                prendre = True
        else:
            if prendre:
                somme += num
            num = 0
            prendre = False

    if prendre:
        somme += num

print(somme)