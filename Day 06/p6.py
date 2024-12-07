f = open("input6.txt", "r")
t = int(f.readline().split(":")[1].replace(" ", ""))
d = int(f.readline().split(":")[1].replace(" ", ""))

print(t, d)

nb = 0
for j in range(t):
    dist = j * (t - j)
    if dist > d:
        nb += 1


print(nb)