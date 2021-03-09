import sys

n = int(sys.stdin.readline().rstrip())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 각 시간 단위에 3이 포함되어 있으면 count 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

