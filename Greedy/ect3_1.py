gsr = 1260
result = 0

coin_list = [500, 100, 50, 10]

for i in coin_list:
    result += gsr // i
    gsr %= i

print(result)