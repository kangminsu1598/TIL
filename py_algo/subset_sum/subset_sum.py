import sys
sys.stdin = open("subset_sum_input.txt", "r")

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    arr = list(range(1,13))
    n = len(arr)
    count = 0
    for i in range(1 << n):
        sum = 0
        result = []
        for j in range(n):
            if i & (1 << j):
                sum += arr[j]
                result.append(arr[j])
        print(result)

        # if sum == K and len(result) == N:
        #     count += 1

    # print(f"#{tc + 1} {count}")