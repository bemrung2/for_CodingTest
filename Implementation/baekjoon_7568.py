import sys

num = int(sys.stdin.readline().rstrip())

people = []

for _ in range(num):
    w, h = map(int ,sys.stdin.readline().rstrip().split())
    people.append((w, h))

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")



