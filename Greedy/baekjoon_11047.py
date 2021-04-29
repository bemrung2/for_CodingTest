import sys

n, k = map(int, sys.stdin.readline().split())

ai = []
for i in range(n):
    ai.append(int(sys.stdin.readline()))

ans = 0 

# for i in range(n):
#     if k > ai[n-1-i]:
#         ans += (k // ai[n-1-i])
#         k = k & ai[n-1-i]


while k>0:
    if k // ai[n-1] > 0:
        ans += k // ai[n-1]
        k = k % ai[n-1]
    n -= 1
print(ans)