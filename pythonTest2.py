exist = 0
T = 0
N = []
M = []
text = []
W = []
currentTextLine = 0
result=[]


def func(y, x, yd, xd, t):
    global exist
    cek = 0
    for i in range(1, len(W[t])):
        if 0 <= y+i*yd < N[t] and 0 <= x+i*xd < M[t]:
            if W[t][i] == text[currentTextLine+i*yd][x+i*xd]:
                cek += 1
        else:
            break
    if cek == len(W[t])-1:
        exist += 1

while not 1 <= T <= 100:
    T = int(input())
for t in range(T):
    N.append(int(input()))
    M.append(int(input()))
    while not 1 <= N[t] <= 100 or not 1 <= M[t] <= 100:
        N[t] = int(input())
        M[t] = int(input())
    for x in range(N[t]):
        text.append(input())
    W.append(input())
    while not 1 <= len(W[t]) <= 100:
        W[t] = int(input())
    for y in range(N[t]):
        for x in range(M[t]):
            if W[t][0] == text[currentTextLine][x]:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        func(y, x, i, j, t)
        currentTextLine += 1
    result.append(exist)
    exist=0
for x in range(len(result)):
    print(f"Case {x+1}: {result[x]}")