import sys
sys.stdin = open("binarysearch_input.txt", "r")

T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int,input().split())

    start_a = 1
    start_b = 1
    page_list = range(P)
    end_a = len(page_list)
    end_b = len(page_list)
    count_a = 0
    count_b = 0

    while start_a <= end_a:
        c = int((start_a + end_a) / 2)
        if page_list[c] == Pa:
            count_a += 1
            break
        elif page_list[c] < Pa:
            start_a = c
            count_a += 1
        else:
            end_a = c
            count_a += 1

    # print(count_a)
    # print(start_a)
    # print(end_a)

    while start_b <= end_b:
        c = int((start_b + end_b) / 2)
        if page_list[c] == Pb:
            count_b += 1
            break
        elif page_list[c] < Pb:
            start_b = c
            count_b += 1
        else:
            end_b = c
            count_b += 1

    sol = ''
    if count_a == count_b:
        sol = 0
    elif count_a > count_b:
        sol = 'B'
    else:
        sol = 'A'

    print(f"#{tc + 1} {sol}")
    # print(count_b)
    # print(start_b)
    # print(end_b)