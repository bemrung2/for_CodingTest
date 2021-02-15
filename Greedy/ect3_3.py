import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

result = 0
for i in range(n):
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    min_num = min(num)
    result = max(result, min_num)

print(result)
