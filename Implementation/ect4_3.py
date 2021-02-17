import sys

input_data = sys.stdin.readline().rstrip()
# row는 입력값을 그대로 int형으로
row = int(input_data[1])
# col은 문자형태이므로 ord함수를 통해 숫자로 변환 -> a에 해당하는 아스키코드값을 뺀 후 1을 더해 숫자로 변환
col = int(ord(input_data[0])) - int(ord('a')) + 1


# 나이트가 이동할 수 있는 모든 경우의 수의 리스트 생성
step_list = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 결과값 초기화
result = 0

# 8가지 방향 중 이동이 가능한 방향 탐색
for step in step_list:
    if row + step[0] < 1 or col + step[1] < 1 or row + step[0] > 8 or col + step[1] > 8:
        continue
    result += 1

print(result)

