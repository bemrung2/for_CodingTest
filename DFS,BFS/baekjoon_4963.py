import sys
sys.setrecursionlimit(10000) # 메모리초과 해결
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]


while True:
    w, h = map(int,input().split())
    if w == 0:
        break
    island = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    
    def dfs(x, y):
        visited[x][y] = True
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            if island[nx][ny]== 1 and visited[nx][ny] is False:
                dfs(nx,ny)
                
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1 and visited[i][j] is False:
                dfs(i,j)
                cnt += 1
    print(cnt)