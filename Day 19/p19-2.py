d = {}
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

def compte(interval, pos = "in"):
    if pos == "R":
        return 0 #Ils sont tous rejetés
    if pos == "A": #Ils sont tous acceptés
        produit = 1
        for min, max in interval.values():
            produit *= max - min + 1
        return produit
    
    regles = d[pos]

    total = 0

    for cle, signe, valeur, resultat in regles:
        if cle != "":
            borneInf, borneSup = interval[cle]
            if signe == "<":
                intervalOK = (borneInf, valeur - 1) # -1 car inférieur strict
                intervalKO = (valeur, borneSup)
            elif signe == ">":
                intervalOK = (valeur +1, borneSup)
                intervalKO = (borneInf, valeur)

            if intervalOK[0] <= intervalOK[1]: # Si l'interval contient au moins une valeur
                copie = dict(interval)
                copie[cle] = intervalOK
                total += compte(copie, resultat)
            if intervalKO[0] <= intervalKO[1]:
                interval[cle] = intervalKO

        else:
            total += compte(interval, resultat)

    return total



print(compte({key: (1, 4000) for key in "xmas"}))