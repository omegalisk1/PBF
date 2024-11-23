import random
a=random.sample(range(1,10001), 1000)
b=random.sample(range(1,10001), 1000)
b.sort()
fileOut = open("x.in", "w")
for x in b:
    fileOut.write(f"{x}\n")
for x in a:
    fileOut.write(f"{x}\n")
fileOut.close()