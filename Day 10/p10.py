from collections import deque

sortie = {
    "|": ["N", "S"],
    "-": ["O", "E"],
    "L": ["N", "E"],
    "J": ["N", "O"],
    "7": ["S", "O"],
    "F": ["S", "E"],
    "S": ["N", "S", "E", "O"],
    ".": []
}

def chemin(map, sX, sY):
    aVisiter = deque()
    aVisiter.append((sX, sY, 0))
    maxDist = 0

    while aVisiter:
        (curX, curY, curD) = aVisiter.popleft()
        
        if maxDist < curD:
            maxDist = curD

        if 0 <= curX-1 and "N" in sortie[map[curX][curY]] and "S" in sortie[map[curX-1][curY]]:
            aVisiter.append((curX-1, curY, curD+1))
        if curX+1 < len(map) and "S" in sortie[map[curX][curY]] and "N" in sortie[map[curX+1][curY]]:
            aVisiter.append((curX+1, curY, curD+1))
        if 0 <= curY-1 and "O" in sortie[map[curX][curY]] and "E" in sortie[map[curX][curY-1]]:
            aVisiter.append((curX, curY-1, curD+1))
        if curY+1 < len(map[curX]) and "E" in sortie[map[curX][curY]] and "O" in sortie[map[curX][curY+1]]:
            aVisiter.append((curX, curY+1, curD+1))
                
        map[curX][curY] = "."

    return maxDist

map = []

indice = 0
f = open("input10.txt", "r")
for x in f:
    map.append(list(x))
    if 'S' in x:
        start = (indice, x.find('S'))

    indice +=1

print(chemin(map, start[0], start[1]))