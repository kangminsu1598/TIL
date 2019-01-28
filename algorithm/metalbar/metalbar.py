import sys
sys.stdin = open("metalbar_input.txt", "r")

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    screws = []
    for i in range(len(data)):
        if i % 2 == 0:
            screws.append(data[i:i+2])
    # print(data)
    # print(screws)

