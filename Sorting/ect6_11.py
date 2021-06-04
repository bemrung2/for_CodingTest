import sys
n = int(sys.stdin.readline().rstrip())

array = []

for i in range(n):
    a,b = sys.stdin.readline().rstrip().split()
    array.append((a, int(b)))

array_sort = sorted(array, key = lambda x : x[1])

for i in range(len(array_sort)):
    print(array_sort[i][0], end = ' ')
