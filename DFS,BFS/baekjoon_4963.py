import sys
sys.setrecursionlimit(10000) # 메모리초과 해결

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0:
        break
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    def dfs(x,y):
        visited[x][y] = 1
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                dfs(i,j)
                cnt += 1
    print(cnt)

# import sys
# sys.setrecursionlimit(10000) # 메모리초과 해결

# dx = [1, -1, 0, 0, 1, -1, -1, 1]
# dy = [0, 0, -1, 1, 1, 1, -1, -1]


# while True:
#     w, h = map(int, sys.stdin.readline().split())
#     if w == 0:
#         break
#     graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
#     visited = [[0] * w for _ in range(h)]
    
#     def dfs(x, y):
#         visited[x][y] = 1
#         for i in range(8):
#             nx, ny = x+dx[i], y+dy[i]
#             if nx<0 or nx>=h or ny<0 or ny>=w:
#                 continue
#             if graph[nx][ny]== 1 and visited[nx][ny] == 0:
#                 dfs(nx,ny)
                
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1 and visited[i][j] == 0:
#                 dfs(i,j)
#                 cnt += 1
#     print(cnt)







# import sys
# sys.setrecursionlimit(10000) # 메모리초과 해결

# dx = [1, -1, 0, 0, 1, -1, -1, 1]
# dy = [0, 0, -1, 1, 1, 1, -1, -1]

# while True:
#     w, h = map(int, sys.stdin.readline().split())
#     if w == 0:
#         break
#     graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
#     visited = [[0] * w for _ in range(h)]
    
#     def dfs(x, y):
#         visited[x][y] = 1
#         for i in range(8):
#             nx, ny = x+dx[i], y+dy[i]
#             if nx<0 or nx>=h or ny<0 or ny>=w:
#                 continue
#             if graph[nx][ny]== 1 and visited[nx][ny] == 0:
#                 dfs(nx,ny)
                
#     cnt = 0
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1 and visited[i][j] == 0:
#                 dfs(i,j)
#                 cnt += 1
#     print(cnt)

