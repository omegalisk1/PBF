import sys
total = 0


def binary_search(array, value, low, high):
    if high <= low:
        return -1
    else:
        mid = int((low + high)/2)
        if array[mid] > value:
            return binary_search(array, value, low, mid)
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid


sys.setrecursionlimit(100000)
array = []
fileIn = open("input.in", "r")
for i in range(10000):
    array.append(fileIn.readline().replace("\n", ""))
for i in range(10000):
    value = fileIn.readline().replace("\n", "")
    print(f"DICARI {value}")
    for j in range(10000):
        if (array[j] == value):
            total += 1
            print(f"FOUND array[{j}] {value}")
            break
print(f"Total : {total}")
