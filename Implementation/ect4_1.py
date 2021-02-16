import sys	

n = int(sys.stdin.readline().rstrip())	
plans = sys.stdin.readline().rstrip().split()	

x, y = 1, 1	

# L, R, U, D에 관한 리스트 작성	
dx = [0, 0, -1, 1]	
dy = [-1, 1, 0, 0]	
move_list = ['L', 'R', 'U', 'D']	
for plan in plans:	
    for i in range(len(move_list)):	
        if plan == move_list[i]:	
            new_x = x + dx[i]	
            new_y = y + dy[i]	
            
    # 공간 밖으로의 이동은 무시
    if new_x < 1 or new_y < 1 or new_x > n or new_y > n:	
        continue

    # 이동이 다음 이동에 영향을 주므로(누적되므로) 반복문 마지막에 꼭 필요함
    x, y = new_x, new_y	


print(x, y) 