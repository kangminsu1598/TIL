import sys
sys.stdin = open("회문_input.txt", "r")

T = int(input())
for tc in range(T):
    # 데이터 받기
    N, M = map(int,input().split())
    data = [[0 for x in range(N)] for x in range(N)]
    for i in range(N):
        data[i] = list(input())
    # print(N, M)
    # print(data)


    # 행 방향 탐색
    for x in range(len(data)):
        row = []
        for y in range(len(data[x])):
            row += data[x][y]
            count = 0
        for idx in range(N-M+1):
            M_list = []
            if row[idx] == row[idx + M - 1]:
                M_list = row[idx:idx + M]
                result = row[idx:idx + M]
                for i in range(len(M_list)//2):
                    M_list[i], M_list[-1-i] = M_list[-1-i], M_list[i]
                if result == M_list:
                    result = ''.join(M_list)
                    print(f'#{tc+1} {result}')


    # 열 방향 탐색
    for y in range(len(data[0])):
        column = []
        for x in range(len(data)):
            column += data[x][y]
            count = 0
        for idx in range(N-M+1):
            M_list = []
            if column[idx] == column[idx + M - 1]:
                M_list = column[idx:idx + M]
                result = column[idx:idx + M]
                for i in range(len(M_list)//2):
                    M_list[i], M_list[-1-i] = M_list[-1-i], M_list[i]
                if result == M_list:
                    result = ''.join(M_list)
                    print(f'#{tc+1} {result}')


    # 행 방향탐색
    # for y in range(len(data)):
    #     row = []
    #     for x in range(len(data[y])):
    #         row += data[y][x]
    #         count = 0
    #     for idx in range(len(row)//2):
    #         count += 1
    #         M_list = []
    #         result = []
    #         if idx < N-M+1:
    #             if row[idx] == row[idx+M-1]:
    #                 M_list = row[idx:idx+M]
    #                 result = row[idx:idx+M]
    #                 result[idx-count+1], result[idx-count] = result[idx-count], result[idx-count+1]
    #                 if M_list == result:
    #                     print(M_list)
    #         else:
    #             idx = len(row)//2 - 1
