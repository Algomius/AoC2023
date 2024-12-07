l = [[], [], [], [], [], [], []]
seeds = ""
lib = ""
f = open("input5.txt", "r")
for x in f:
    if x.find("seeds:") >= 0:
        seeds = (x.split(":"))[1].split()
        seeds = list(map(int, seeds))
    elif x.find("map") >= 0:
        lib = x
    elif x != "":
        m = x.split()
        if len(m) == 3:
            if lib.find("seed-to-soil map:") >= 0:
                l[0].append((int(m[0]), int(m[1]), int(m[2])))
            elif lib.find("soil-to-fertilizer map:") >= 0:
                l[1].append((int(m[0]), int(m[1]), int(m[2])))
            elif lib.find("fertilizer-to-water map:") >= 0:
                l[2].append((int(m[0]), int(m[1]), int(m[2])))
            elif lib.find("water-to-light map:") >= 0:
                l[3].append((int(m[0]), int(m[1]), int(m[2])))
            elif lib.find("light-to-temperature map:") >= 0:
                l[4].append((int(m[0]), int(m[1]), int(m[2])))
            elif lib.find("temperature-to-humidity map:") >= 0:
                l[5].append((int(m[0]), int(m[1]), int(m[2])))
            elif lib.find("humidity-to-location map:") >= 0:
                l[6].append((int(m[0]), int(m[1]), int(m[2])))

minimum = float("Inf")
for i in range(0,len(seeds),2):
    e = seeds[i]
    while e < seeds[i]+seeds[i+1]:
        margeMax = seeds[i]+seeds[i+1]-1-e
        temp = e
        for transfo in range(0, 7):
            test = False
            indice = 0
            while not test and indice < len(l[transfo]):
                delta = temp - l[transfo][indice][1]
                if 0 <= delta < l[transfo][indice][2]:
                    test = True
                    temp = delta + l[transfo][indice][0] 
                    if margeMax > l[transfo][indice][2] - delta - 1:
                        margeMax = l[transfo][indice][2]  - delta - 1
                indice += 1


        if minimum > temp:
            minimum = temp

        if margeMax > 0:
            e += margeMax
        else:
            e += 1

print(minimum)
    

