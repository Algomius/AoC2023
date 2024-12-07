def rollNorth(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'O':
                indice = 1
                while 0 <= i-indice and m[i-indice][j] == '.':
                    indice += 1

                indice -= 1
                m[i - indice][j], m[i][j] = m[i][j], m[i- indice][j]

def rollSouth(m):
    for i in range(len(m)-1, -1, -1):
        for j in range(len(m[i])):
            if m[i][j] == 'O':
                indice = 1
                while i+indice < len(m) and m[i+indice][j] == '.':
                    indice += 1

                indice -= 1
                m[i + indice][j], m[i][j] = m[i][j], m[i+ indice][j]

def rollWest(m):
    for j in range(len(m[0])):
        for i in range(len(m)):
            if m[i][j] == 'O':
                indice = 1
                while 0 <= j-indice and m[i][j-indice] == '.':
                    indice += 1

                indice -= 1
                m[i][j-indice], m[i][j] = m[i][j], m[i][j-indice]

def rollEast(m):
    for j in range(len(m[0])-1, -1, -1):
        for i in range(len(m)):
            if m[i][j] == 'O':
                indice = 1
                while j+indice < len(m[0]) and m[i][j+indice] == '.':
                    indice += 1

                indice -= 1
                m[i][j+indice], m[i][j] = m[i][j], m[i][j+indice]

                

m = []

f = open("input14.txt", "r")
for x in f:
    x = x[:-1]
    m.append(list(x))

t = tuple(tuple(e) for e in m)
dejaVu = {t}
l = [t]

test = True
indice = 0

while test:
    indice += 1
    rollNorth(m)
    rollWest(m)
    rollSouth(m)
    rollEast(m)
    t = tuple(tuple(e) for e in m)
    if t in dejaVu:
        test = False
    else:
        dejaVu.add(t)
        l.append(t)

debutCycle = l.index(t)
longueurCycle = indice - debutCycle

posFinale = ((1000000000 - debutCycle) % longueurCycle) + debutCycle
t = l[posFinale]
taille = len(t)
somme = 0
for e in t:
    for i in e:
        if i == 'O':
            somme += taille
    taille -= 1

print(somme)

