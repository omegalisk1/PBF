T = 0
N = 0
M = 0
map = []
results = []
faction = None
factionsList = []
contested = 0


def surveying(y, x):
    global faction
    global factionNumber
    if (y >= 0 and y < N) and (x >= 0 and x < M):
        if map[y][x] != "#" and map[y][x] != "0":
            if map[y][x].isalpha():
                if faction == None:
                    faction = map[y][x]
                elif faction !=map[y][x]:
                    faction = "multi"
            map[y][x] = "0"
            surveying(y+1, x)
            surveying(y-1, x)
            surveying(y, x+1)
            surveying(y, x-1)


def processingData():
    global faction
    global contested
    global factionsList
    if faction == "multi":
        contested += 1
        faction = None
    elif faction != None:
        if len(factionsList) == 0:
            factionsList.append([])
            factionsList[len(factionsList)-1].append(faction)
            factionsList[len(factionsList)-1].append(1)
            faction = None
        else:
            for i in range(len(factionsList)):
                if factionsList[i][0] == faction:
                    factionsList[i][1] = int(factionsList[i][1]+1)
                    faction = None
                    break
            if faction != None:
                factionsList.append([])
                factionsList[len(factionsList)-1].append(faction)
                factionsList[len(factionsList)-1].append(1)
                faction = None


file = open("input.in", "r")
T = int(file.readline())
for t in range(T):
    N = (int(file.readline()))
    M = (int(file.readline()))
    for y in range(N):
        map.append([])
        read = file.readline().replace("\n", "")
        for x in range(M):
            map[y].append(read[x])
    for y in range(N):
        for x in range(M):
            if map[y][x].isalpha():
                surveying(y, x)
                processingData()
    factionsList.sort()
    print(f"Case {t+1}:")
    for y in range(len(factionsList)):
        print(f"{factionsList[y][0]} {factionsList[y][1]}")
    print(f"contested {contested}")
    map = []
    factionsList = []
    contested = 0
