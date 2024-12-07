from sympy import symbols, solve

grelon = []
f = open("input24.txt", "r")
for x in f:
    x  = x[:-1]
    coordonnees, velocite = x.split('@')
    c = list(map(int, coordonnees.split(',')))
    v = list(map(int, velocite.split(',')))
    grelon.append((c, v))



# https://www.youtube.com/watch?v=guOyA7Ijqgk
# chaque grelon part d'une position xinit et se trouvera à une position xt après un temps t : xt = xinit + t*vx
# il en est de même pour la pierre lancée : xpt = xpinit + t*vxp
# s'il ya collision, il y a donc au temps t, égalité des x : xpinit + t*vpt = xinit + t*vt et donc t = (xinit - xpinit) / (vxp - vx) 
# et pareil pour y et z : t = (yinit - ypinit) / (vyp - vy) et t = (zinit - zpinit) / (vzp - vz)
# Ces 3 ratios sont donc égaux (car tous = t)

# les inconnues sont les positions et la vélocité de la pierre lancée, les autres données sont connues

xjet, yjet, zjet, vxjet, vyjet, vzjet = symbols("xjet, yjet, zjet, vxjet, vyjet, vzjet")   

equations = [] 

for e in grelon:
    equations.append((xjet - e[0][0]) * (e[1][1] - vyjet) - (yjet - e[0][1]) * (e[1][0] - vxjet))
    equations.append((yjet - e[0][1]) * (e[1][2] - vzjet) - (zjet - e[0][2]) * (e[1][1] - vyjet))

solution = solve(equations)
print(solution[0][xjet] + solution[0][yjet] + solution[0][zjet])
    


                
