map = []
doubleLine = []
doubleCol = []
galaxy= []
removeCol = []

indice = 0
f = open("input11.txt", "r")
for x in f:
    map.append(list(x[:-1]))
    if x.find('#') < 0:
        doubleLine.append(indice)
    else:
        for j in [i for i, letter in enumerate(x) if letter == "#"]:
            galaxy.append((indice, j))
            if j not in removeCol:
                removeCol.append(j)
            
    indice += 1

for i in range(len(map[0])):
    if i not in removeCol:
        doubleCol.append(i)

print (galaxy)
print(doubleLine)
print(doubleCol)

somme = 0
cpt = 0
for i1 in range(len(galaxy)-1):
    for i2 in range(i1+1, len(galaxy)):
        g1 = galaxy[i1]
        g2 = galaxy[i2]
        for i in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
            if i in doubleLine:
                somme += 1000000
            else:
                somme += 1
        for i in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
            if i in doubleCol:
                somme += 1000000
            else:
                somme += 1
        cpt +=1

print(cpt)              
print(somme)