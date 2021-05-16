import sys

n = int(sys.stdin.readline())

agen = []
for i in range(n):
    agen.append(list(map(int, sys.stdin.readline().split())))

# agen2 = sorted(agen, key = lambda x : x[0])
# agen3 = sorted(agen, key = lambda x : x[1])
agen4 = sorted(agen, key = lambda x : (x[1], x[0]))

# agen = sorted(agen, key = lambda x : x[0])
# agen = sorted(agen, key = lambda x : x[1])

# print(agen)
# print(agen2)
# print(agen3)
# print(agen4)

last = 0
cnt = 0
# print(agen)
for i, j in agen4:
    if i >= last:
        cnt += 1
        last = j

print(cnt)

# # 궁금증 
# for i, j in agen:
#     print(i,end='')
#     print(j,end='')

# 가장 최대 경우의 수를 찾는게 아니라
# 일단 가장 빠른 회의가 시작되고 난 뒤에 
# 최대의 경우의 수를 찾는거임
# 즉 input 4 / 1 7 / 2 3 / 4 5 / 5 7 -> 3이 아니라 1이 나옴.