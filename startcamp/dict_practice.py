# 파이썬 dictionary 활용 기초!

#1. 평균을 구하자
scores = {
    "철수": {
        "국어": 80,
        "영어": 90,
        "수학": 100
    },
    "영희": {
        "수학": 70,
        "국어": 60,
        "음악":50
    }
}

#sol 1-1
# start = 0 # 시작을 리스트 말고 값으로 만드는 생각이 중요!!!!!!
# for score in dict.values(scores):
#     # start = start + i/len(dict.values(scores))
#     start += score/len(dict.values(scores))
# print(start)

#sol 1-2
# total_score = sum(scores.values())

#2. 반 평균을 구하자
# #so1 2-1
# total = 0
# for name in scores:
#     for score in scores[name].values():
#         total += score/len(scores[name])

# print(total/len(scores))

# #so1 2-2
# total = 0
# count = 0
# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total += indivisual_score
#         count += 1
# print(total/count)

# 반복 딕셔너리 키 밸류
# for i, n in scores.items(): #for문에서 딕셔너리 사용시 변수가 2개면 각 변수마다 키 밸류 할당한다
#     print(i)
#     print(n)

#3 도시 중에 최근 3일 중 가장 추웠던 곳, 가장 더웠던 곳?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

# 변수를 생각하고 if를 돌려서 기준 값을 만드는 게 포인트
hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0


# for 문으로 기준값을 입력한다

for name, temp in citise.items():
    if (count==0):
        hot = max(hot)
        cold = min(cold)
        hot_city = name
        cold_city = name
        
    else:
        if (cold > )
        dd
    count += 1

            










for name, temp in cities.items():

    if (count == 0):
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        if (min(temp) < cold):
            cold = min(temp)
            cold_city = name
        if (max(temp) > hot):
            hot = max(temp)
            hot_city = name
    count += 1

print(f"{hot_city},{cold_city}")



#변수명 name, temp

# for name, temp in cities.items():


    
