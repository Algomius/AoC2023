from collections import deque

def parcours(m, pos, nbMouv):
    aVisiter = deque([(pos[0], pos[1], nbMouv)])
    lstValid = set()
    dejaVu ={(pos[0], pos[1])}
    while aVisiter:
        x, y, d= aVisiter.popleft()
        if d % 2 == 0:
            lstValid.add((x, y))
        if d == 0:
            continue

        for voisinX,voisinY  in [[x + 0,y + 1], [x+ 0,y-1], [x-1, y+0], [x+1, y+0]]:
            if 0 <= voisinX < len(m) and 0 <= voisinY < len(m[0]):
                if m[voisinX][voisinY] != '#' :
                    if (voisinX, voisinY) not in dejaVu:
                        dejaVu.add((voisinX, voisinY))
                        aVisiter.append((voisinX, voisinY, d-1))

    return(len(lstValid))


m = []
indice = 0
f = open("input21.txt", "r")
for x in f:
    x  = x[:-1]
    if x.find('S') != -1:
        start = (indice, x.find('S'))
    m.append(list(x))
    indice += 1

#Vérification : https://www.youtube.com/watch?v=9UOMZSL0JTg

# Taille de la map : la map est un carré (131 * 131) et le point de départ est le centre de la map
#print(len(m), len(m[0]))
#print(start)
    
# la taille du déplacement est un multiple de la taille de la map + la position du point de départ
# print(26501365 % 131)
# On va donc parcourir jusqu'au bout d'une map dans toutes les directions
# On cherche également le nombre maximum de grilles dans chaque direction 
# print(26501365 // 131)
# On ne peut donc pas le faire en itératif

# La ligne et la colonne du point de départ sont vide (pas de bloc)
# Les colonnes et lignes extérieurs sont vides (ca va servir pour la propagation)
# On peut donc parcourir cette ligne et cette colonne en ligne droite et on peut atteindre le point le plus éloigné, 
#à 26501365 déplacement du point de départ

# Si le nombre de déplacement est impair, on ne peut plus se rendre au point de départ, par contre, on peut se rendre au centre des 
# grilles adjacentes car il y a un nombre de déplacements impair entre les deux centres
# On peut trouver les carrés similaires à partir de leur centre

# On commence par calculer les carrés complets :
longueur_map = len(m)
longueur_chemin = 26501365
taille_grille = longueur_chemin // longueur_map - 1 # -1 car le dernier carré n'est pas complet

# On calcul les carrés complets identiques à la map de départ
nb_grille_depart = (taille_grille // 2 * 2 + 1 ) ** 2 # // 2 * 2 permet de faire un arrondi a l'entier pair

# On calcul les carrés complets différents de la map de départ
nb_grille_different = ((taille_grille + 1) // 2 * 2) ** 2

#print(nb_grille_depart, nb_grille_different) - OK

# On calcule maintenant une grille identique et une grille différente
nb_points_depart = parcours(m, start, longueur_map * 2 + 1) # Le dernier paramètre est un nombre impair assez grand pourcouvrir la grille
nb_points_different = parcours(m, start, longueur_map * 2)

#print(nb_points_depart, nb_points_different)

somme = 0

# On ajoute les points obtenu sur les grilles identiques a celle de depart 
somme += nb_grille_depart * nb_points_depart
# On ajoute les points obtenu sur les grilles differentes a celle de depart 
somme += nb_grille_different * nb_points_different

# On s'occupe des 4 maps des points cardinaux N, S, E, O. On sait que l'on commence au milieu du carré et qu'il rest assez de mouvement pour
# aller sur l'arrête opposée soit longueur_grille-1
caseN = parcours(m, (longueur_map-1, start[1]),  longueur_map-1)
somme += caseN
caseS = parcours(m, (0, start[1]),  longueur_map-1)
somme += caseS
caseO = parcours(m, (start[0], longueur_map-1),  longueur_map-1)
somme += caseO
caseE = parcours(m, (start[0], 0),  longueur_map-1)
somme += caseE

# Il reste à calculer les map découpées en diagonale, a chaque fois, il y a un petit triangle et un polygone a 5 côtés

#Commençons par le petit triangle, lorsque l'on arrive dans l'angle droit du triangle, il reste en déplacement 

# taille - 1 : deplacement restant a la base des caseN....
# taille - 1 - taille/2 = taille/2 - 1 : quand on arrive dans le triangle

# comme pour les cardinaux il y a 4 types de triangles
 
triangleNE = parcours(m, (longueur_map-1, 0),  longueur_map // 2 -1)
triangleNO = parcours(m, (longueur_map-1, longueur_map-1),  longueur_map // 2 -1)
triangleSE = parcours(m, (0, 0),  longueur_map // 2 -1)
triangleSO = parcours(m, (0, longueur_map-1),  longueur_map // 2 -1)

# chacun de ces triangles arrive : longueur_grille +1 
somme += (triangleNE + triangleNO + triangleSE + triangleSO) * (taille_grille +1) 

# Le raisonnement est le même pour les pentagones. Seule la distance de départ change, il reste 3/2 de taille -1

pentagoneNE = parcours(m, (longueur_map-1, 0),  longueur_map * 3 // 2 -1)
pentagoneNO = parcours(m, (longueur_map-1, longueur_map-1),  longueur_map * 3 // 2 -1)
pentagoneSE = parcours(m, (0, 0),  longueur_map * 3 // 2 -1)
pentagoneSO = parcours(m, (0, longueur_map-1),  longueur_map * 3 // 2 -1)

# Chacun des pentagone arrive : longueur_grille

somme += (pentagoneNE + pentagoneNO + pentagoneSE + pentagoneSO) * taille_grille 

print(somme)