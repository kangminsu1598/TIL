import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(T):
    N = list(map(int, input().split()))
    number = list(map(int, input()))
    c = [0] * 10
    for i in range(len(number)):
        c[number[i]] += 1

    my_max = c[0]
    my_index = 0
    for index, element in enumerate(c):
        if element >= my_max:
            my_max = element
            my_index = index

    print(f"#{tc + 1} {my_index} {my_max}")