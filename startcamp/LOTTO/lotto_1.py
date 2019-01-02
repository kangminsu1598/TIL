from bs4 import BeautifulSoup
import requests
import random


numbers = random.sample(range(800, 838), 8)
for num in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    lucky = soup.select(".ball_645")
    print(f"{num}회차 당첨번호")
    for i in lucky:
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()
    
# for i in range(0,8):
#     numbers_index = numbers[i]
#     main_num = []
#     bonus_num = []
#     req = requests.get(f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={numbers_index}").text
#     soup = BeautifulSoup(req, "html.parser")
#     for tag in soup.select(".article > div:nth-child(2) > div > div.win_result > div"):
#         main_num = tag.select_one(".div.num.win > p > span.ball_645.lrg.ball").text
#         bonus_num = tag.select_one(".div.num.bonus > p > span").text
#         print(f"{main_num} + {bonus_num}")
#     print(f"{numbers_index}회차 당첨번호")

