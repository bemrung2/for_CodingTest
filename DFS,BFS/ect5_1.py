# 파이썬에서 스택은 별도의 라이브러리를 사용하지 않아도 됨
# 기본 리스트에서 append()와 pop() 메서드를 이용하면
# 스택 자료구조와 동일하게 동작하기 때문이다.
## 선입후출 or 후입선출
stack = []

stack.append(5)
print(stack)

stack.append(2)
print(stack)

stack.append(3)
print(stack)

stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.append(1)
print(stack)

stack.append(4)
print(stack)

stack.pop()
print(stack)

# 최상위 원소부터 출력
print(stack[::-1])