# 무식한 방법
# bit = [0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)

# 비트연산자

arr = [-7, -3, -2, 5, 8]
n = len(arr)

# i는 부분집합의 위치, 수, j는 인덱스 번호
for i in range(1 << n):
    sum = 0
    result = []
    for j in range(n):
        if i & (1 << j):
            sum += arr[j]
            result.append(arr[j])
    if sum == 0 and result != []:
        print(result)

