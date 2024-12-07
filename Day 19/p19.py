def nextRule(ep, d, pos):
    for e in d[pos]:
        if e[1] == '>':
            if ep[e[0]] > e[2]:
                return e[3]
        elif e[1] == '<':
            if ep[e[0]] < e[2]:
                return e[3]
        else:
            return e[3]



d = {}
p = []
testPiece = False
f = open("input19.txt", "r")
for x in f:
    if x.find('{') == -1:
        testPiece = True
    elif not testPiece:
        x = x[:-1]
        l = x.split("{")
        name = l[0]
        d[name] = []
        rules = l[1][:-1]
        for e in rules.split(","):
            if e.find(":") != -1:
                condition, resultat = e.split(":")
                cle = condition[0]
                signe = condition[1]
                valeur = int(condition[2:])
                d[name].append((cle, signe, valeur, resultat))
            else:
                d[name].append(("", "", "", e))
    else:
        x = x[1:-2]
        dic = {}
        for e in x.split(","):
            i = e.split("=")
            dic[i[0]] = int(i[1])
        p.append(dic)

somme = 0
for ep in p:
    pos = 'in'
    while pos != 'A' and pos != 'R':
        pos = nextRule(ep, d, pos)

    if pos == 'A':
        somme += ep['x'] + ep['m'] + ep['a'] +ep['s'] 

print(somme)