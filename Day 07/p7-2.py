def fiveOf(s):
    return s[0] == s[4]

def fourOf(s):
    return (s[0] == s[3]) or (s[1] == s[4])

def fullhouse(s):
    return (s[0] == s[2] and s[4] == s[3]) or (s[0] == s[1] and s[2] == s[4])

def threeOf(s):
    return (s[0] == s[2]) or (s[1] == s[3])  or (s[2] == s[4])

def twoPairs(s):
    return (s[0] == s[1] and s[2] == s[3]) or (s[0] == s[1] and s[3] == s[4] )  or (s[2] == s[1] and s[4] == s[3] )

def onePairs(s):
    return s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or s[3] == s[4]

def getVal(s):
    s_sorted = ''.join(sorted(s))
    reste = ""
    cptJ = 0

    for e in s_sorted:
        if e == "J":
            cptJ += 1
        else:
            reste += e
    if cptJ == 5 or cptJ == 4:
        return 6
    elif cptJ == 3:
        if reste[0] == reste[1]:
            return 6
        else:
            return 5
    elif cptJ == 2:
        if reste[0] == reste[2]:
            return 6
        elif reste[0] == reste[1] or reste[1] == reste[2]:
            return 5
        else:
            return 3
    elif cptJ == 1:
        if reste[0] == reste[3]:
            return 6
        elif reste[0] == reste[2] or reste[1] == reste[3]:
            return 5
        elif reste[0] == reste[1] and reste[2] == reste[3]:
            return 4
        elif reste[0] == reste[1] or reste[1] == reste[2] or reste[2] == reste[3]:
            return 3
        else:
            return 1
    elif fiveOf(s_sorted):
        return 6
    elif fourOf(s_sorted):
        return 5
    elif fullhouse(s_sorted):
        return 4
    elif threeOf(s_sorted):
        return 3
    elif twoPairs(s_sorted):
        return 2
    elif onePairs(s_sorted):
        return 1
    else:
        return 0

def inverse(c1, c2):
    dict = {
        "A" : 14, 
        "K" : 13, 
        "Q" : 12, 
        "J" : 1, 
        "T" : 10, 
        "9" : 9,
        "8" : 8,
        "7" : 7,
        "6" : 6,
        "5" : 5, 
        "4" : 4, 
        "3" : 3,
        "2" : 2
    }

    h1 = getVal(c1[0])
    h2 = getVal(c2[0])

    if h1 > h2:
        return True
    elif h2 > h1:
        return False
    else:
        for i in range(len(c1[0])):
            if dict[c1[0][i]] > dict[c2[0][i]]:
                return True
            elif dict[c1[0][i]] < dict[c2[0][i]]:
                return False
        
        return False 


m = []

f = open("input7.txt", "r")
for x in f:
    m.append(x.split())

changement = True
while changement:
    changement = False
    for i in range(len(m)-1):
        if inverse(m[i], m[i+1]):
            m[i], m[i+1] = m[i+1], m[i]
            changement = True
indice = 1
somme = 0
for e in m:
    somme += indice * int(e[1])
    indice += 1

print(somme)

