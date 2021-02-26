import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):
    # 조건을 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 해당 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상하좌우 위치 모두 <재귀적으로> 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)