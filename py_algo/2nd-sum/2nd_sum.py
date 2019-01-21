import sys
sys.stdin = open("input.txt", "r")


for tc in range(10):
    N = list(map(int, input().split()))
    arr = [[0 for x in range(100)] for x in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    # 행의 합
    sum_line = 0
    for y in arr:
        if sum_line < sum(y):
            sum_line = sum(y)

    # 열의 합
    sum_row = 0
    for x in range(len(arr[0])):
        middle = 0
        for y in range(len(arr)):
            middle += arr[y][x]
        if sum_row < middle:
            sum_row = middle

    # 대각선의 합
    sum_1 = 0
    sum_2 = 0
    for i in range(0, len(arr)):
        sum_1 += arr[i][i]
        sum_2 += arr[i][99-i]

    # 합 비교
    my_max = max(sum_line, sum_row, sum_1, sum_2)

    print(f"#{tc + 1} {my_max}")
