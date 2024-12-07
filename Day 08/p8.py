seq = ""
path = {}
invpath = {}

debut = ""
fin = ""
f = open("input8.txt", "r")
for x in f:
    if seq == "":
        seq = x[:-1]
    elif x != "" and x.find("=") >= 0:
        dir = x.split("=")
        if not path:
            debut = dir[0].replace(" ", "")
        dest = dir[1][2:-2].split(",")
        path[dir[0].replace(" ", "")] = (dest[0].replace(" ", ""), dest[1].replace(" ", ""))
        fin = dir[0].replace(" ", "")
        invpath[dest[0].replace(" ", "")].append((dir[0].replace(" ", ""), "L"))
        invpath[dest[0].replace(" ", "")].append((dir[1].replace(" ", ""), "R"))

debut, fin= fin, debut
temp = debut
indice = 0
while temp != fin:
    if seq[indice % (len(seq))] == "L":
        temp = path[temp][0]
    else:
        temp = path[temp][1]
    indice +=1

print(indice)