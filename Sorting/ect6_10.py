import sys

n = int(sys.stdin.readline().rstrip())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

sort_array = (sorted(array, reverse=True))

for i in range(len(sort_array)):
    print(sort_array[i], end= ' ')