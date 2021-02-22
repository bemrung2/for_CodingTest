from collections import deque

queue = deque()

queue.append(5)
print(queue)

queue.append(2)
print(queue)

queue.append(3)
print(queue)

queue.append(7)
print(queue)

queue.popleft()
print(queue)

queue.append(1)
print(queue)

queue.append(4)
print(queue)

queue.popleft()
print(queue)

# 역순으로 출력하기
queue.reverse()
print(queue)

# 리스트 자료형으로 변경하고자 한다면
a = list(queue)
print(a)