import sys
sys.stdin = open("special_sort_input.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    result = []

    for i in range(len(data)-1):
        max = i
        for j in range(i+1,len(data)):
            if data[max] < data[j]:
                data[max], data[j] = data[j], data[max]

    if len(data) % 2 == 0:
        for idx in range(5):
            result.append(data[idx])
            result.append(data[N-1-idx])

    print(f"#{tc + 1} {' '.join(list(map(str,result)))}")

    # if len(data) % 2 == 0:
    #     for idx in range(len(data)//2):
    #         result.append(data[idx])
    #         result.append(data[N-1-idx])
    # else:
    #     for idx in range(len(data)//2):
    #         result.append(data[idx])
    #         result.append(data[N-1-idx])
    #     result.append(data[len(data)-len(data)//2])