import sys

n = int(sys.stdin.readline())

ans = 0

while n >= 0:
    if n % 5 == 0:
        ans += (n // 5)
        print(ans)
        break
    n -= 3
    ans += 1
else:
    print(-1)


# left = n%5
# mok = int(n/5)
# final_mok = int(left/3)

# final = final_mok + mok

# if n%3 != 0 and n%5 != 0:
#     print(-1)
# elif (n%5) % 3 != 0:
#     print(int(n/3))
# else:
#     print(final)




# # n은 3과 5로 만들수있어야함

