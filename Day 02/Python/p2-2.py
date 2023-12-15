cube = {
    "blue": 0,
    "green": 0,
    "red": 0
}

somme = 0
f = open("input2.txt", "r")
for x in f:
    cube["blue"] = 0
    cube["green"] = 0
    cube["red"] = 0
    y = x.split(":")[1]
    for z in y.split(";"):
        for a in z.split(","):
            b = a.split()
            if int(b[0]) > cube[b[1]]:
                cube[b[1]] = int(b[0])

    somme += cube["blue"] * cube["green"] * cube["red"]

print(somme)
    