#자연수 n, 1~n까지 한줄에 하나씩 출력
# item = int(input("번호를 입력하세요"))
# for i in range(1,item+1):
#     print(i)

# 투자 경고 종목 리스트 사용자로부터 종목명을 입력 받은 후 종목이 투자 경고 종목이라면 투자 경고 종목입니다.
#아니면 투자 경고 종목이 아닙니다를 출력

# warn_investment_list = ['ms','google','naver','kakao','samsung','lg']
# print(f"경고 종목 리스트 : {warn_investment_list}")
# item = input("투자 종목이 무엇입니까? : ")
# if item.lower() in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")
    
# colors = ['apple','banana','coconut','deli','ele','grape']
# fruit = []

# for i in range(len(colors)):
#     if i in [0, 4, 5]:
#         pass
#     else:
#     colors.append(colors[i])

# print(colors2)

# deleteindex = [0, 4, 5]
# for i in range(0, len(colors)):
#     if i not in deleteindex:
#         fruit.append(colors[i])
# print(fruit)

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}
print(ssafy["duration"]["semester1"])
print(ssafy["location"][1])
print(ssafy["classes"]["daejeon"]["manager"])