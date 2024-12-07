from collections import deque
import math

flipflop = {}
conjunction = {}
broadcast = []

f = open("input20.txt", "r")
for x in f:
    x  = x[:-1]
    machine, output =  x.split("->")
    if machine[0] == '%':
        flipflop[machine[1:].replace(" ","")] = ["off",  output.replace(" ","").split(",")]
    elif machine[0] == '&':
        conjunction[machine[1:].replace(" ","")] = [{}, output.replace(" ","").split(",")]
    else:
        for e in output.split(","):
            broadcast.append(e.replace(" ",""))

l = []
for e in flipflop.keys():
    for x in flipflop[e][1]:
        if x == 'rx':
            l.append(e)
        if x in conjunction.keys():
            conjunction[x][0][e] = 'low'

for e in conjunction.keys():
    for x in conjunction[e][1]:
        if x == 'rx':
            l.append(e)
        if x in conjunction.keys():
            conjunction[x][0][e] = 'low'

for i in broadcast:
    if i == 'rx':
        l.append(e)
    if i in conjunction.keys():
        conjunction[x][0]['broadcaster'] = 'low'

if len(l)> 1 :
    print("Cela devient compliqué de trouver une solution")

longueur_cycle = {}
dejaVu = {nom : 0 for nom in conjunction[l[0]][0].keys()}

fin = False
nbPush = 0
while not fin:
    nbPush += 1
    d = deque()
    d.append(('button', 'low', 'broadcaster'))
    while d:
        begin, pulse, end = d.popleft()

        if end == l[0] and pulse == "high":
            dejaVu[begin] += 1

            if begin not in longueur_cycle:
                longueur_cycle[begin] = nbPush

            if all(dejaVu.values()):
                x = 1
                for lc in longueur_cycle.values():
                    x = math.lcm(x, lc)
                print(x)
                exit(0)

        if end == 'broadcaster':
            for x in broadcast:
                d.append(('broadcaster', pulse, x))
        elif end in flipflop.keys():
            if pulse == 'low':
                if flipflop[end][0] == "off":
                    flipflop[end][0] = "on"
                    for x in flipflop[end][1]:
                        d.append((end, "high", x))
                else:
                    flipflop[end][0] = "off"
                    for x in flipflop[end][1]:
                        d.append((end, "low", x))
        elif end in conjunction.keys():
            conjunction[end][0][begin] = pulse
            test = True
            for x in conjunction[end][0].keys():
                if conjunction[end][0][x] == 'low':
                    test = False
            for x in conjunction[end][1]:
                if test:
                    d.append((end, "low", x))
                else:
                    d.append((end, "high", x))
