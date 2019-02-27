import sys
sys.stdin = open("compare_input.txt", "r")

T = int(input())
for tc in range(T):
    # 1이 패턴 2는 전체
    str1 = input()
    str2 = input()



    # while 문으로
    def bruteforce(p, t):
        i = 0
        j = 0
        while j < len(p) and i < len(t):
            if t[i] != p[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1

        if j == len(p):
            return 1
        else:
            return 0

    print(f"#{tc+1} {bruteforce(str1, str2)}")

    # def my_comparison(str1, str2):
    #     # 패턴 찾을 경우 첫 시작 값 idx
    #     idx = 0
    #     diff = 0
    #     for i in range(len(str2)):
    #         for j in range(len(str1)):
    #             if str1[j] != str2[i]:
    #                 j = 0
    #                 diff = 0
    #                 idx += 1
    #                 break
    #             else:
    #                 i += 1
    #                 diff += 1
    #         if len(str1) == diff:
    #             return 1
    #     if diff != len(str1):
    #         return 0
    # print(f"#{tc+1} {my_comparison(str1, str2)}")