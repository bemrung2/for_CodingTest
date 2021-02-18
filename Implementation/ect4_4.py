import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

# 리스트 컴프리핸션을 통해 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, sys.stdin.readline().rstrip().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction # direction 변수가 함수 바깥에서 선언된 전역변수라 global 키워드 사용
    direction -= 1
    if direction == -1:
        direction = 3
    
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)