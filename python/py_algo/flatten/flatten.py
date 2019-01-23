import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1):
    N = int(input())
    data = list(map(int, input().split()))

# 정렬한다.

def my_sort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# 최대값 원소를 찾아서 1을 빼고 최소값 원소에 1을 더한다.
    aver = int(sum(data)/100)
    print(data)
    print(aver)


    diff = my_max - my_min
    count = 0
    hundred = [100] * 100
    while count < N:
        for i in range(100)
            if data[i] > aver:
                data[i] -= 1
                count += 1



        count += 1
    else:
        return diff
