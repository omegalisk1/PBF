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
fileOut = open("output.in", "w")
for i in range(10000):
    array.append(fileIn.readline().replace("\n", ""))
for i in range(10000):
    value = fileIn.readline().replace("\n", "")
    print(f"DICARI {value}")
    answer = binary_search(array, value, 0, 9999)
    if answer != -1:
        total += 1
    fileOut.write(f"{answer}\n")
    print(f"FOUND array[{answer}] {value}")
print(f"Total : {total}")
fileIn.close()
fileOut.close()