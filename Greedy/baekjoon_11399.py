import sys

n = int(sys.stdin.readline())
pi = list(map(int, sys.stdin.readline().split()))

pi.sort()
result = 0


for i in range(n):
    for j in range(i+1):
        result += pi[j]

print(result)

