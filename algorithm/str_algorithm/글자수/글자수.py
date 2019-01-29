import sys
sys.stdin = open("글자수_input.txt", "r")

T = int(input())
for tc in range(T):
    str1 = str(input())
    str2 = str(input())

    ans = []
    for i in str1:
        ans.append(str2.count(i))

    print(f'#{tc+1} {max(ans)}')




# T = int(input())
# for tc in range(T):
#     pattern = input()
#     data = input()
#     data_dict = {}
#     for element in data:
#         if element not in data_dict:
#             data_dict.update({element: 1})
#         else:
#             data_dict[element] += 1
#     print(data)
#     print(data_dict)
#     my_max = 0
#     for key, value in data_dict.items():
#         if my_max < value:
#             my_max = value
#     print(my_max)
#

