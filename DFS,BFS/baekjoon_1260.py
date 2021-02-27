import sys

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0 for i in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = 0 # dfs 실행 시 방문처리 되어있기에 여기서 0으로 초기화
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)


