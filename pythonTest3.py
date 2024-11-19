T = 0
N = 0
M = 0
map = []
results = []
faction = None
factionsList = []
contested = 0
import sys


def surveying(y, x):
    global faction
    global factionNumber
    if (y >= 0 and y < N) and (x >= 0 and x < M):
        if map[y][x] != "#" and map[y][x] != "0":
            if map[y][x].isalpha():
                if faction == None:
                    faction = map[y][x]
                elif faction != map[y][x]:
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
        if len(factionsList) != 0:
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

sys.setrecursionlimit(100000) 
fileIn = open("input.in", "r")
fileOut = open("output.in", "w")
T = int(fileIn.readline())
for t in range(T):
    N = (int(fileIn.readline()))
    M = (int(fileIn.readline()))
    for y in range(N):
        map.append([])
        read = fileIn.readline().replace("\n", "")
        for x in range(M):
            map[y].append(read[x])
    for y in range(N):
        for x in range(M):
            if map[y][x].isalpha():
                surveying(y, x)
                processingData()
    factionsList.sort()
    fileOut.write(f"Case {t+1}:\n")
    for y in range(len(factionsList)):
        fileOut.write(f"{factionsList[y][0]} {factionsList[y][1]}\n")
    fileOut.write(f"contested {contested}\n")
    map = []
    factionsList = []
    contested = 0
fileIn.close()
fileOut.close()