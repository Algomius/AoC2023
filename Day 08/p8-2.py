from math import gcd
seq = ""
path = {}

debut = []
fin = []

f = open("input8.txt", "r")
for x in f:
    if seq == "":
        seq = x[:-1]
    elif x != "" and x.find("=") >= 0:
        dir = x.split("=")
        dest = dir[1][2:-2].split(",")
        depart = dir[0].replace(" ", "")
        arriveeL=dest[0].replace(" ", "")
        arriveeR=dest[1].replace(" ", "")
        path[depart] = {}
        path[depart]["L"] = arriveeL
        path[depart]["R"] = arriveeR
        if depart[-1] == "A":
            debut.append(depart)
        elif depart[-1] == "Z":
            fin.append(depart)



print(debut)
print(fin)
temp = debut
indice = 0

cycle = [-1] * len(debut)
nbTrouve = 0

while nbTrouve < len(cycle):
    letter = seq[indice % (len(seq))]
    indice +=1
    for i in range(len(temp)):
        temp[i] = path[temp[i]][letter]
        if temp[i] in fin and cycle[i] == -1:
            cycle[i] = indice
            nbTrouve += 1


# Calcul du plus grand commun multiple de tous les chemins
lcm = 1
for i in cycle:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)