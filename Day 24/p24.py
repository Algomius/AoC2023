def dejaPasse(g, x, y):
    if g[0][0] < x and g[1][0] < 0:
        return True
    
    if g[0][0] > x and g[1][0] > 0:
        return True
    
    if g[0][1] < y and g[1][1] < 0:
        return True
    
    if g[0][1] > y and g[1][1] > 0:
        return True
    
    return False
    

testArea = {
    "x" : (200000000000000, 400000000000000),
    "y" : (200000000000000, 400000000000000)
}

grelon = []
f = open("input24.txt", "r")
for x in f:
    x  = x[:-1]
    coordonnees, velocite = x.split('@')
    c = list(map(int, coordonnees.split(',')))
    v = list(map(int, velocite.split(',')))
    a = v[1] / v[0]    # coeficient directeur de la fonction affine
    b = c[1] - (a*c[0]) # constante b de la fonction affine
    grelon.append((c, v, (a, b)))

nbChocs = 0
for i in range(len(grelon)):
    for j in range(i+1, len(grelon)):
        g1 = grelon[i]
        g2 = grelon[j]
        if g1[2][0] == g2[2][0] : # coefficient directeur identique, elles sont parallèles
            print("Parallèle : ", g1, " - ", g2)
        else:
            x = (g2[2][1] - g1[2][1]) / (g1[2][0] - g2[2][0]) # calcul de x a partir de a1x+b1 = ax2 + b2
            y = g1[2][0] * x + g1[2][1]

            if testArea["x"][0] <= x <= testArea["x"][1] and testArea["y"][0] <= y <= testArea["y"][1]:
                if not dejaPasse(g1, x, y) and not dejaPasse(g2, x, y):
                    print("Intersection : ", g1, " - ", g2, " --> x= ", x, " y= ", y)
                    nbChocs += 1

print(nbChocs)

                
