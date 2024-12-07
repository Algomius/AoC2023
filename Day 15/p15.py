def getBox(s):
    res = 0
    for i in s:
        res += ord(i)
        res *= 17
        res %= 256

    return res

lBox = [{} for _ in range(256)]
f = open("input15.txt", "r")
for x in f:
    x = x[:-1]
    l = x.split(",")
    for e in l:
        if e[-1] == "-":
            cle = e[:-1]
            boxNb = getBox(cle)
            remValue = lBox[boxNb].pop(cle, None)
            if remValue != None:
                for cle, valeur in lBox[boxNb].items():
                    if lBox[boxNb][cle][1] > remValue[1]:
                        lBox[boxNb][cle] = (lBox[boxNb][cle][0], lBox[boxNb][cle][1]-1)
        else:
            eq = e.split("=")
            boxNb = getBox(eq[0])
            if eq[0] in lBox[boxNb].keys():
                lBox[boxNb][eq[0]] = (int(eq[1]), lBox[boxNb][eq[0]][1])
            else :
                lBox[boxNb][eq[0]] = (int(eq[1]), len(lBox[boxNb]))

somme = 0
for i in range(len(lBox)):
    for cle, valeur in lBox[i].items():
        somme += ((i + 1) * (valeur[1] + 1)  * valeur[0])

print(somme)

