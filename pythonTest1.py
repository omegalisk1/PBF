t=0
while not 1<=t<=100:
    t=int(input())
a=[]
b=[]
k=[]
for x in range(t):
    a.append(int(input()))
    b.append(int(input()))
    k.append(int(input()))
    while not 1<=k[x]<10000 or not 1<=a[x]<=b[x]<10000:
        a[x]=int(input())
        b[x]=int(input())
        k[x]=int(input())
for x in range(t):
    if a[x]%k[x]==0:
        res=1
    else:
        res=0
    res=res+int((b[x]-a[x])/k[x])
    case=f"Case {x+1}: {res}"
    print(case)