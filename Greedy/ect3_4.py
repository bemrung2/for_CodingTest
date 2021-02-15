import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
result = 0

while True:
    temp_target = (n//k) * k
    result += (n - temp_target)
    n = temp_target
    if n < k:
        break
    result += 1
    n //= k
    
result += (n-1)

print(result)

