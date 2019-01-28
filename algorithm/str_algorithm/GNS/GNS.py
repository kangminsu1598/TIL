import sys
sys.stdin = open("GNS_input.txt", "r")

T = int(input())
for tc in range(10):
    temp = input() #더미 데이터
    data = list(map(str, input().split()))

    num_list =["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    values = [0]*10
    # values에 데이터에서 뽑은 값의 호출된 횟수를 저장한다
    for idx in range(len(data)):
        if data[idx] in num_list:
            values[num_list.index(data[idx])] += 1

    # num_list와 values의 인덱스마다 곱연산해서 출력한다
    print(f"#{tc + 1}")
    for idx in range(len(values)):
        print((num_list[idx]+' ') * values[idx])



