import sys

node = int(sys.stdin.readline().rstrip())
rel = int(sys.stdin.readline().rstrip())
# 인덱스 번호를 맞추기 위해 한 줄 추가
graph = [[0]*(node+1) for _ in range(node+1)]


for _ in range(rel):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    # 대칭이므로 각각 1을 넣어줌
    graph[x][y], graph[y][x] = 1,1 

visited = []
def dfs(v):
    visited.append(v)
    for i in range(1, node+1):
        if (i not in visited) and (graph[v][i] ==1):
            dfs(i)
    return (len(visited)-1)
    

print(dfs(1))
