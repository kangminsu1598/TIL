import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    my_max = data[-1]
    my_min = data[0]

    print(f"#{tc + 1} {my_max-my_min}")