import random
import requests
import json
from pprint import pprint # json 거쳐야 적용가능 

# pprint(lotto)
# print(type(lotto))


# 0. random으로 로또 번호 생성합니다.
# 1. api를 통해 우승 번호를 가져옵니다.
# 2. 0번과 1번을 비교하여 나의 등수를 알려준다.

# 1. url 요청 보내서 가져오기
#     - json으로 받는다. (딕셔너리로 접근 가능)
# 2. api의 당첨번호와 보너스번호를 저장하고
# 3. 뽑은게 몇등인지, 몇번만에 1등 당첨된건지 코드 구성

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

# main_num = []
# for i in range(1,7):
#     one_num = lotto.get(f"drwtNo{i}")
#     main_num.append(one_num)

# bonus_num = [(lotto["bnusNo"])] # int 값이라 합치리면 스트링 써야함


# count = 0
# both_ok = 0
# bonus_ok = 0
# while both_ok < 7:
#     my_num = sorted(random.sample(range(1,46),6))
#     both_ok = len(set(my_num) & set(main_num))
#     bonus_ok = len(set(my_num) & set(bonus_num))

#     print("보너스 번호 : " + str(bonus_num))
#     print("이번 주 당첨번호 : " + str(main_num))
#     count += 1
#     if both_ok == 6:
#         print("1등입니다.")
#         print(f"참가횟수는 {count}입니다")
#         money = count*1000
#         print(f"{money}써서 당첨입니다")
#         break
#     elif both_ok == 4:
#         print("4등입니다.")
#     elif both_ok == 5:
#         print("3등입니다.")
#         if bonus_ok == 1:
#             print("2등입니다.")
#     else:
#         print("아쉽게도 당첨되지 않았습니다.")

# while true:
#     if matched == 6:
#         print("1등")
#     elif matched == 5:
#         if bonus in my_numbers:
#             print("2등")
#         else:
#             print("3등")
#     elif matched == 4:
#         print("4등")
#     elif matched == 3:
#         print("5등")
#     else:
#         print("꽝")



