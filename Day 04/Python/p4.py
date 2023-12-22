somme = 0
f = open("input4.txt", "r")
for x in f:
    y = x[:-1].split("|")
    gagnant = (y[0].split(":"))[1].split()
    carte = y[1].split()
    pts = 0
    for e in carte:
        if e in gagnant:
            if pts == 0:
                pts = 1
            else:
                pts *= 2
    somme += pts
print(somme)

