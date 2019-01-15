import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(T):
    info = list(map(int, input().split()))
    data = list(map(int, input().split()))
    N = info[0]
    M = info[1]
    my_sum = []

    for i in range(len(data)-M+1):
        my_sum += [sum(data[i:i+M])]
    result = max(my_sum) - min(my_sum)

    print(f"#{tc + 1} {result}")