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

    front = screws[0][0]
    back = screws[0][1]
    n = len(screws)
    answer = [screws[0]]
    for i in range(1, n):
        j = 1
        while j < n:
            if screws[j] not in answer:
                if back == screws[j][0]:
                    back = screws[j][0]
                    answer.append(screws[j])
                elif front == screws[j][1]:
                    front = screws[j][1]
                    answer.insert(0, screws[j])
                j = 0
            j += 1
    print(answer)


    # forward = screws[0][0]
    # backward = screws[0][1]
    # for y in range(1,len(screws)):
    #     for x in range(len(screws[y])):
    #         if x == 0:
    #             if screws[y][x] == backward:
    #                 # screws[y], screws[y-1] = screws[y-1], screws[y]
    #                 backward = screws[y][1]
    #         if x == 1:
    #             if screws[y][x] == forward:
    #                 screws[y], screws[y-1] = screws[y-1], screws[y]
    #                 forward = screws[y][0]
    # print(screws)




