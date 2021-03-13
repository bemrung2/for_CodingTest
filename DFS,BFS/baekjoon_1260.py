from collections import deque
import sys

# n : 노드 / m : 간선 / v : 시작노드
n, m, v = map(int, sys.stdin.readline().rstrip().split())


graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = graph[b][a] = 1

visited = [False] * (n+1)
def dfs(v):
    visited[v] = True
    print(v, end= ' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == True:
                queue.append(i)
                visited[i] = False


        

dfs(v)
print()
bfs(v)


# from collections import deque
# import sys
# n, m, v = map(int, sys.stdin.readline().rstrip().split())

# graph = [[0] * (n+1) for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     graph[a][b] = graph[b][a] = 1

# visited = [False] * (n+1)

# def dfs(v):
#     visited[v] = True
#     print(v, end= ' ')
#     for i in range(1, n+1):
#         if visited[i] == False and graph[i][v] == 1:
#             dfs(i)

# def bfs(v):
#     queue = deque([v])
#     visited[v] = False
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in range(1, n+1):
#             if visited[i] == True and graph[i][v] == 1:
#                 queue.append(i)
#                 visited[i] = False

    
# dfs(v)
# print()
# bfs(v)

# n, m, v = map(int, sys.stdin.readline().rstrip().split())

# # graph = [list(map(int, list(sys.stdin.readline().rstrip().split()))) for _ in range(m)]
# graph = [[0] * (n+1) for _ in range(n+1)] # 한 칸씩 추가로 생성 (인덱스를 그대로 사용하기 위함) 
# for _ in range(m):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     graph[x][y] = graph[y][x] = 1

# visited = [False] * (n+1)
# def dfs(v):
#     visited[v] = True
#     print(v, end = ' ')
#     for i in range(1, n+1):
#         if (visited[i] == False) and (graph[v][i] == 1):
#             dfs(i)

# dfs(v)

# def bfs(v):
#     queue = deque([v])
#     visited[v] = False  # 앞에서 True로 했기 때문에 bfs에서는 반대로 진행한다.
#     while queue:
#         v = queue.popleft()
#         print(v, end = ' ')
#         for i in range(1, n+1):
#             if visited[i] == True and graph[v][i] ==1:
#                 queue.append(i)
#                 visited[i] = False

# print()
# bfs(v)


# from collections import deque
# import sys

# n, m, v = map(int, sys.stdin.readline().rstrip().split())
# matrix = [[0] * (n+1) for i in range(n+1)]
# for i in range(m):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     matrix[x][y] = matrix[y][x] = 1


# visited = [False] * (n+1)

# def dfs(v):
#     visited[v] = True
#     print(v, end= ' ')
#     for i in range(1, n+1):
#         if visited[i] == False and matrix[v][i] == 1:
#             dfs(i)

# from collections import deque
# def bfs(v):
#     queue = deque([v])
#     visited[v] = False
#     while queue:
#         v = queue.popleft()
#         print(v, end = ' ')
#         for i in range(1, n+1):
#             if visited[i] == True and matrix[v][i] ==1:
#                 queue.append(i)
#                 visited[i] = False

# dfs(v)
# print()
# bfs(v)


# import sys

# n, m, v = map(int, sys.stdin.readline().rstrip().split())
# graph = [[0] * (n+1) for _ in range(n+1)]
# visited = [0 for i in range(n+1)]

# for _ in range(m):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     graph[x][y] = 1
#     graph[y][x] = 1

# def dfs(v):
#     visited[v] = 1
#     print(v, end = ' ')
#     for i in range(1, n+1):
#         if visited[i] == 0 and graph[v][i] == 1:
#             dfs(i)

# from collections import deque

# def bfs(v):
#     queue = deque([v])
#     visited[v] = 0 # dfs 실행 시 방문처리 되어있기에 여기서 0으로 초기화
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in range(1, n+1):
#             if visited[i] and graph[v][i] == 1:
#                 queue.append(i)
#                 visited[i] = 0 # line 23과 마찬가지

# dfs(v)
# print()
# bfs(v)