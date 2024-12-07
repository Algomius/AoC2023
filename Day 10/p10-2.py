from collections import deque

sortie = {
    "|": ["N", "S"],
    "-": ["O", "E"],
    "L": ["N", "E"],
    "J": ["N", "O"],
    "7": ["S", "O"],
    "F": ["S", "E"],
}

def chemin(map, sX, sY):
    aVisiter = deque()
    aVisiter.append((sX, sY))
    monChemin = []

    while aVisiter:
        (curX, curY) = aVisiter.popleft()
        

        if 0 <= curX-1 and "N" in sortie[map[curX][curY]] and "S" in sortie[map[curX-1][curY]] and (curX-1, curY) not in monChemin:
            aVisiter.append((curX-1, curY))
        if curX+1 < len(map) and "S" in sortie[map[curX][curY]] and "N" in sortie[map[curX+1][curY]] and (curX+1, curY) not in monChemin:
            aVisiter.append((curX+1, curY))
        if 0 <= curY-1 and "O" in sortie[map[curX][curY]] and "E" in sortie[map[curX][curY-1]] and (curX, curY-1) not in monChemin:
            aVisiter.append((curX, curY-1))
        if curY+1 < len(map[curX]) and "E" in sortie[map[curX][curY]] and "O" in sortie[map[curX][curY+1]] and (curX, curY+1) not in monChemin:
            aVisiter.append((curX, curY+1))
                
        monChemin.append((curX, curY))

    return monChemin

def donneS(map, sX, sY):

    possibleDir = []
    if 0 <= sX-1 and "S" in sortie[map[sX-1][sY]]:
        possibleDir.append("N")
    if sX+1 < len(map) and "N" in sortie[map[sX+1][sY]]:
        possibleDir.append("S")
    if 0 <= sY-1 and "E" in sortie[map[sX][sY-1]]:
        possibleDir.append("O")
    if sY+1 < len(map[sX]) and "O" in sortie[map[sX][sY+1]]:
        possibleDir.append("E")

    if "N" in possibleDir and "S" in possibleDir:
        return "|"
    if "O" in possibleDir and "E" in possibleDir:
        return "-"
    if "N" in possibleDir and "E" in possibleDir:
        return "L"
    if "N" in possibleDir and "O" in possibleDir:
        return "J"
    if "S" in possibleDir and "O" in possibleDir:
        return "7"
    if "S" in possibleDir and "E" in possibleDir:
        return "F"
    

map = []

indice = 0
f = open("input10.txt", "r")
for x in f:
    map.append(list(x))
    if 'S' in x:
        start = (indice, x.find('S'))

    indice +=1

map[start[0]][start[1]] = donneS(map, start[0], start[1])
c = chemin(map, start[0], start[1])

trouveHori = []
for i in range(len(map)):
    nbBarre = 0
    vuL = False
    vuF = False
    for j in range(len(map[i])):
        if map[i][j] == "|" and (i, j) in c:
            nbBarre += 1
        elif map[i][j] == "L" and (i, j) in c:
            vuL = True
        elif map[i][j] == "F" and (i, j) in c:
            vuF = True
        elif map[i][j] == "J" and (i, j) in c:
            if vuF :
                nbBarre += 1
            vuF = False
            vuL = False
        elif map[i][j] == "7" and (i, j) in c:
            if vuL :
                nbBarre += 1
            vuF = False
            vuL = False
        elif (i, j) not in c and nbBarre%2 == 1:
            trouveHori.append((i, j))

trouveVert = []
for j in range(len(map[0])):
    nbBarre = 0
    vu7 = False
    vuF = False
    for i in range(len(map)):
        if map[i][j] == "-" and (i, j) in c:
            nbBarre += 1
        elif map[i][j] == "7" and (i, j) in c:
            vu7 = True
        elif map[i][j] == "F" and (i, j) in c:
            vuF = True
        elif map[i][j] == "J" and (i, j) in c:
            if vuF :
                nbBarre += 1
            vuF = False
            vu7 = False
        elif map[i][j] == "L" and (i, j) in c:
            if vu7 :
                nbBarre += 1
            vuF = False
            vu7 = False         
        elif (i, j) not in c and nbBarre%2 == 1:
            trouveVert.append((i, j))

print(len(set(trouveHori) & set(trouveVert))) 

