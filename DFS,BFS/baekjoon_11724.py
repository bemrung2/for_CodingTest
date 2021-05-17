import sys
sys.setrecursionlimit(10**8)

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
# visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = graph[y][x] = 1


def dfs(x):
    visited[x] = 1
    for i in range(1, n+1):
        if graph[x][i] == 1 and visited[i] == 0 :
            dfs(i)

cnt = 0 

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)