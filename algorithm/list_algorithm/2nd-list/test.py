# 행 우선순회, i: i행, j: j열
array = [[0,1,2,3]
        ,[4,5,6,7]]
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end='')
    print()

# 열 우선순회
for j in range(len(array[0])):
    for i in range(len(array)):
        print(array[i][j], end='')
    print()

# 지그재그

for i in range(len(array)):
    for j in range(len(array[0])):
        print(array[i][j+(4-1-2*j)*(i%2)], end='')
    print()