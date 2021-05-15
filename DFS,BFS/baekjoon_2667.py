import sys

n = int(sys.stdin.readline().rstrip())

mat = []

for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0 
apt = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x,y):
    global cnt
    mat[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if mat[nx][ny] == 1:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            cnt = 0
            dfs(i,j)
            apt.append(cnt)

apt.sort()

print(len(apt))
for i in range(len(apt)):
    print(apt[i])