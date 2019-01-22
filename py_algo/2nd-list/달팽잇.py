
arr = [
       [9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

for y in range(arr):
    min = arr[y][0]
    for x in range(arr[y]):
        if min > arr[y][x]:
            min = arr[y][x]
            for z in range(x+1,len(arr[y])):
                min, arr[y][z] = arr[y][z], min
print(arr)



