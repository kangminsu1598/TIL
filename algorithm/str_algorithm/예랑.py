import sys
sys.stdin = open("회문_input.txt", "r")

T = int(input())

def hm(x):
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            return False
    return True

for tc in range(T):
    N, M = map(int, input().split())
    data = [input() for i in range(N)]
    x = ''
    # print(data)

    for j in range(N):
        y = ''
        for i in range(N):
            y += data[i][j]
        for z in range(N - M + 1):
            if hm(y[z:M + z]):
                ans = y[z:M + z]
            x = data[j][z:M + z]
            if hm(x):
                ans = x

    print(f'#{tc+1} {ans}')