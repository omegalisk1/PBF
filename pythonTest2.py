exist = 0
T = 0
N = []
M = []
text = []
W = []
currentTextLine = 0
result = []


def func(y, x, t):
    global exist
    for yd in range(-1, 2):
        for xd in range(-1, 2):
            cek = 0
            for i in range(1, len(W[t])):
                if 0 <= y+i*yd < N[t] and 0 <= x+i*xd < M[t]:
                    if W[t][i] == text[currentTextLine+i*yd][x+i*xd]:
                        cek += 1
                else:
                    break
            if cek == len(W[t])-1:
                exist += 1

file = open("input.in", "r")
T = int(file.readline())
for t in range(T):
    N.append(int(file.readline()))
    M.append(int(file.readline()))
    for x in range(N[t]):
        text.append(file.readline().replace("\n",""))
    W.append(file.readline().replace("\n",""))
    for y in range(N[t]):
        for x in range(M[t]):
            if W[t][0] == text[currentTextLine][x]:
                func(y, x, t)
        currentTextLine += 1
    result.append(exist)
    exist = 0
file.close()
file = open("output.in", "w")
for x in range(len(result)):
    file.write(f"Case {x+1}: {result[x]}\n")
file.close()