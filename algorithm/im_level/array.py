Y, X = map(int, input().split())
data = [[0 for x in range(X)] for x in range(Y)]

for i in range(Y):
    data[i] = list(map(int, input().split()))

for i in range(len(data)):
    for j in range(len(data[i])-1,0,-1):
        if data[i][j] == 1:
            value = 1
            while data[i][j] == data[i][j-count] and j-count >= 0:
                value += 1
            data[i][j] = value
        
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()
