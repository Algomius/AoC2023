d = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
}

somme = 0
f = open("input1.txt", "r")
for x in f:
    minDist = len(x)+1
    minVal = 0
    maxDist = -1
    maxVal = 0
    for i in d.keys():
        temp = x.find(i)
        if minDist > temp and temp != -1:
            minDist = temp
            minVal = d[i]

        temp = x.rfind(i)
        if maxDist < temp:
            maxDist = temp
            maxVal = d[i]

    print(x[:-1], " - ", minVal, " - ", maxVal)

    somme += (minVal * 10) + maxVal

print(somme)
     