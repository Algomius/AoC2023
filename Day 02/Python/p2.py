cube = {
    "red": 12,
    "green": 13,
    "blue": 14
}

indice = 1
somme = 0
f = open("input2.txt", "r")
for x in f:
    test = True
    y = x[:-1].split(":")
    for m in y[1].split(";"):
        for a in m.split(","):
            b = a.split()
            qte = int(b[0])
            couleur = b[1]
            if cube[couleur] < qte:
                test = False
    
    if test:
        somme += indice

    indice += 1

print(somme)