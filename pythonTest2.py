baris=3
kolom=4
d="cat"
text=["catt","aata","tatc"]
exist=0

def func(y,x,yd,xd):
    global exist
    cek=0
    for i in range(1,len(d)):
        if 0<=y+i*yd<baris and 0<=x+i*xd<kolom:
            if d[i]==text[y+i*yd][x+i*xd]:
                cek+=1
        else:
            break
    if cek==len(d)-1:
        exist+=1

for y in range(baris):
    for x in range(kolom):
        if d[0]==text[y][x]:
            for i in range(-1,2):
                for j in range(-1,2):
                    func(y,x,i,j)

print(exist)