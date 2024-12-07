def compte(p, c):
    if not p:
        if not c:
            return 1
        else:
            return 0
        
    if not c:
        if "#" in p:
            return 0
        else:
            return 1

    resultat = 0

    if p[0] in ".?":
        resultat += compte(p[1:], c)

    if p[0] in "#?":
        if c[0] <= len(p) and "." not in p[:c[0]] and (c[0] == len(p) or p[c[0]] != "#"):
            resultat += compte(p[c[0] + 1:], c[1:])

    return resultat

somme = 0
f = open("input12.txt", "r")
for x in f:
    line = x[:-1].split(' ')
    chiffre = list(map(int, line[1].split(',')))
    pipes = line[0]

    somme += compte(pipes, chiffre)

print(somme)