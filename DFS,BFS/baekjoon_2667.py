import sys

n = int(sys.stdin.readline().rstrip())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    graph[x][y] = 0
    global cnt
    cnt += 1
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)

lst = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            lst.append(cnt)

lst.sort()

print(len(lst))
for i in range(len(lst)):
    print(lst[i])


# import sys

# n = int(sys.stdin.readline().rstrip())

# mat = []

# for i in range(n):
#     mat.append(list(map(int, sys.stdin.readline().rstrip())))

# cnt = 0 
# apt = []

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# def dfs(x,y):
#     global cnt
#     mat[x][y] = 0
#     cnt += 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or nx >= n or ny < 0 or ny >= n:
#             continue
#         if mat[nx][ny] == 1:
#             dfs(nx,ny)

# for i in range(n):
#     for j in range(n):
#         if mat[i][j] == 1: 
#             cnt = 0
#             dfs(i,j)
#             apt.append(cnt)

# apt.sort()

# print(len(apt))
# for i in range(len(apt)):
#     print(apt[i])