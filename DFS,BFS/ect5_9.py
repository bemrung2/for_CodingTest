from collections import deque

def bfs(graph, start, visited):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드 방문처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue: # = While True
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        

# 각 노드가 연결된 정보를 2차원 리스트 자료형으로 표현
graph = [
    [], # index 0에 대한 내용이므로 비워둠
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)