# 순차 검색
# def sequentialsearch(a, n, key):
#     i = 0
#     while i < n and a[i] != key:
#         i = i + 1
#
#     if i < n : return i
#     else: return -1
#
# data = [4, 9, 11, 23, 2, 19, 7]
# key = 5
# print(sequentialsearch(data, len(data), key))
#

# # 이진 검색
# def binarysearch(a, key):
#     start = 0
#     end = len(a) - 1
#     while start <= end:
#         middle = start + (end-start) // 2
#         if key == a[middle]:
#             return middle
#         elif key < a[middle]:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return -1
#
# key = 7
# data = [2, 4, 7, 9, 11, 19, 23]
# print(binarysearch(data, key))

# 선택 정렬
def selectionsort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[min], a[i] = a[i], a[min]

data = [64, 25, 10, 22, 11]
selectionsort(data)
print(data)