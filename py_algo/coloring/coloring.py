import sys
sys.stdin = open("coloring_input.txt", "r")


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0 for x in range(10)] for x in range(10)]

    for case in range(N):
        data = list(map(int, input().split()))
        if data[4] == 1:
            for y in range(data[0], data[2]+1):
                for x in range(data[1], data[3]+1):
                    arr[y][x] += 1
        else:
            for y in range(data[0], data[2]+1):
                for x in range(data[1], data[3]+1):
                    arr[y][x] += 2

    count = 0
    for i in arr:
        count += i.count(3)

    print(f'#{tc+1} {count}')
# print(arr)