def getNext(l):

    if all(v == 0 for v in l):
        return 0
    else:
        s = []
        for i in range(len(l)-1):
            s.append(l[i+1]-l[i])
        return l[0] - getNext(s)

l = []

somme = 0
f = open("input9.txt", "r")
for x in f:
    somme += getNext(list(map(int, x.split())))

print(somme)