import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

num.sort(reverse=True) # 숫자 솔팅하기

first_num = num[0]
second_num = num[1]

result = 0
first_num_count = int((m/(k+1)*k) + (m%(k+1)))

result += first_num*first_num_count
result += second_num*(m-first_num_count)
print(result)



### 단순하게 풀기

# n, m, k = map(int, sys.stdin.readline().rstrip().split())
# num = list(map(int, sys.stdin.readline().rstrip().split()))
# result = 0

# num.sort(reverse=True) # 숫자 솔팅하기

# first_num = num[0]
# second_num = num[1]


# while True:
#     for i in range(k):
#         if m == 0 :
#             break
#         result += first_num
#         m -= 1
#     if m == 0:
#         break
#     result += second_num
#     m -= 1
# print(result)