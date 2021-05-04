import sys
 
n, k = map(int, sys.stdin.readline().split())

ai = []
for i in range(n):
    ai.append(int(sys.stdin.readline()))

ans = 0 

while k > 0:
    if k > ai[n-1]:
        ans += k // ai[n-1]
        k = k % ai[n-1]
    n -= 1


# ans = 0 

# while k>0:
#     if k // ai[n-1] > 0:
#         ans += k // ai[n-1]
#         k = k % ai[n-1]
#     n -= 1




# for i in range(n-1, -1, -1):
#     if k == 0:
#         break
#     if ai[i] > k:
#         continue
#     ans += k // ai[i]
#     k = k % ai[i]
    



print(ans)