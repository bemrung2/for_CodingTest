import sys
sys.setrecursionlimit(10000)
# t = int(sys.stdin.readline().rstrip())

# m, n, k = map(int, sys.stdin.readline().rstrip().split())

# graph = [[0] * n for _ in range(m)]

# for _ in range(k):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     graph[a][b] = 1


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    graph[x][y] = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= m or nx < 0 or ny >= n or ny < 0:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)

# cnt = 0

# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs(i,j)
#             cnt += 1

# print(cnt)

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().rstrip().split())

    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1
    
    print(cnt)

