

arr = [[0 for x in range(5)] for x in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

sum = 0

def iswall(x,y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

def calabs(x,y):
    if y > x:
        return y - x
    else:
        return x - y

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for y in range(len(arr)):
    for x in range(len(arr[y])):
        for i in range(4):
            testx = x + dx[i]
            testy = y + dy[i]
            if iswall(testx,testy) == False:
                sum += calabs(arr[y][x], arr[testy][testx]
                # arr[y][x]가 행렬 외곽에 있는 원소를 index하면 arr[testy][testx]가 list range 에러