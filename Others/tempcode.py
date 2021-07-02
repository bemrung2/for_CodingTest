import sys
sys.setrecursionlimit(10**8)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    array[x][y] = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if array[nx][ny] == 1:
            dfs(nx, ny)

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    result = 0
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    array = [[0] * (n) for _ in range(m)]

    for i in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        array[a][b] = 1


    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:
                dfs(i,j)
                result += 1
    print(result)



    

    



# import sys
# print(sys.version)

# n = int(sys.stdin.readline().rstrip())

# array = []
# for i in range(n):
#     a, b = sys.stdin.readline().rstrip().split()
#     array.append([a,int(b)])

# array.sort(key = lambda x : x[1])
# print(array)

# for i in range(n):
#     print(array[i][0], end=' ')




# import sys
# n = int(sys.stdin.readline().rstrip())

# array = []

# for i in range(n):
#     a,b = sys.stdin.readline().rstrip().split()
#     array.append((a, int(b)))

# array_sort = sorted(array, key = lambda x : x[1])

# for i in range(len(array_sort)):
#     print(array_sort[i][0], end = ' ')

# for i in array_sort:
#     print(array_sort[0], end = ' ')



# import sys

# n = int(sys.stdin.readline().rstrip())
# array = []

# for i in range(n):
#     array.append(int(sys.stdin.readline().rstrip()))

# sort_array = (sorted(array, reverse=True))

# for i in range(len(sort_array)):
#     print(sort_array[i], end= ' ')


# ''' 퀵 정렬 - 파이썬의 장점을 곁들인 '''

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


# def quick_sort(array):
#     # 리스트가 하나 이하의 워소만을 담고 있다면 종료
#     if len(array) <= 1:
#         return array

#     pivot = array[0]
#     tail = array[1:] # 피벗을 제외한 리스트

#     left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
#     right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
#     # print(left_side)
#     # print([pivot])
#     # print(right_side)


#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)


# print(quick_sort(array))
# a = [1,2,3,4,5]
# b = [5,6,7,8]

# print(set(a)-set(b)

''' 리스트 차집합

lst1 = ['A', 'B', 'C', 'D']
lst2 = ['C', 'D', 'E', 'F']
complement = list(set(lst1) - set(lst2))
print( complement ) # ['B', 'A'] 


# #컨트롤 쉬프트 L 혹은 컨트롤 H
'''

# def solution(n, lost, reverse):
#     reverse_del = set(reverse) - set(lost)
#     lost_del = set(lost) - set(reverse)

#     for i in reverse_del:
#         if i-1 in lost_del:
#             lost_del.remove(i-1)
#         elif i+1 in lost_del:
#             lost_del.remove(i+1)

#     return n-len(lost_del)


# def solution(n, lost, reserve):
#     reser_del = set(reserve)-set(lost)
#     lost_del = set(lost)-set(reserve)
    
#     for i in reser_del:
#         if i-1 in lost_del:
#             lost_del.remove(i-1)
#         elif i+1 in lost_del:
#             lost_del.remove(i+1)
    
#     return n-len(lost_del)