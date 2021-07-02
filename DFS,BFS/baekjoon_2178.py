import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 방향 벡터 선언
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽 무시
            if graph[nx][ny] == 0: 
                continue
            # 해당 노드를 처음 방문해야만 최단거리
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))

