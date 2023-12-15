somme = 0
f = open("input1.txt", "r")
for x in f:
    x = x[:-1]
    premier = ""
    dernier = ""
    for c in x:
        if "1" <= c <= "9":
            if premier == "":
                premier = c
            dernier = c

    somme += int(premier + dernier)

print(somme)
     