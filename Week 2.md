# Week2_

## Class1. 파이썬 기초와  git

### 1. 파이썬 문법



- | 저장  | 대상                   |
  | ----- | ---------------------- |
  | what? | 글자, 숫자, 참/거짓    |
  | how?  | 변수, 리스트, 딕셔너리 |

- 조건

  - if문

    - ```if문
      if ~:
      	~~~~
      elif ~:
      	~~~~
      ```

- 반복

  - while문

    - while에 해당할 동안 계속 반복

    - 종료 조건 필수

    - ```ㄹㄹ
      while ~:
      	~~~~
      ```

  - for문

    - 정해진 범위에서 실행되므로 종료조건 필요없음

    - ```for in 구문
      for i in dust:
      	print(i)
      ```

### 2. git의 작업flow

> 작업 > 커밋할 목록 > 쌓인 커밋들 > Github

- add : 커밋할 목록에 추가
- commit : 커밋(Create a snapshot) 만들기
- 현재까지의 역사(Commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기



## Class2. Web의 구조와 Web 스크래핑

### 1. 웹 스크래핑

> 하나하나씩 내용물 찍어보면서 진행!

- requests

```
import requests
req = requests.get("https://www.google.com")
print(req)
print(req.text)
print(req.status_code)
```

#### 1-1. 정보 스크랩 1단계

1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다.

```
import requests
req = requests.get("https://www.google.com").text
```

2. 정보를 출력하여 확인한다.

```
print(req)
```

#### 1-2. 정보 스크랩 2단계

1. 정보를 조작하기 편하게 바꾸고,

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(req, 'html.parser')
```

2. 바꾼 정보 중 원하는 것만 뽑아서,

```
kospi = soup.select_one(‘selector 경로’)
```

3. 출력한다

```
print(kospi.text)
```



## Class3. Flask를 활용한 어플리케이션 구축

### 1. Flask

> Micro Framework
>
> django : Full stack Framework
>
> flask 접속 : c9.io/login

```
@app.route(/math/<int:num>)
def math(num):
	result = num**3
	return render_template("math_html", math_num = num, math_result = result)	
```

#### 1-1 flask html

> from flask import Flask, render_template : Flask와 외장함수를 호출한다.
>
> route : 웹 주소를 할당
>
> def : name 함수를 정의 : name 값을 입력하는 함수
>
> return : 값을 전달한다, render_template(외장함수, 템플릿에 변수를 전달하는 함수) 함수를 사용해서 입력받은 변수(name)을 html의 your_name에 전달
>
> html : 입력받은 정보를 출력하는 기능
>
> string : 문자변수, int : 숫자변수



## Class 4. Dictionary

### 1. Dictionary

- 자료형에서 특정 값을 불러오고 싶을 때 사용

![img](https://lh5.googleusercontent.com/hbbEyOhDc1Fec5UpEzSFwVuuvTYS3M7IeL2YdxfzaOvbCLfIfrYKZAeW0TTgN-9FD4h3f9H3bOw3LnpF8D82Fj2eXMqjpJhMTpW-HTpPb49y81rWXPX3s0RSwEiH9HTlggdQZG7x)

- how to use? => 각 KEY와 VALUES를 지정하여 불러오면 됨!


## Class 5. LOTTO 프로그램 & 텔레그램 챗봇 만들기 

### 1. LOTTO 프로그램 만들기

- **"내가 로또에 당첨되려면 얼마나 많은 돈을 투자해할지" 파이썬을 통해 구하기 **
  - 6개의 당첨 번호를 뽑고
  - 최신 당첨 번호와 비교해 1등에 당첨되기위해 투자해야하는 **MONEY ** & **횟수**  *FIND*

### 2. 텔레그램 챗봇 만들기

- ***텔레그램이 나에게 챗봇으로 실시간 미세먼지 농도를 알려준다면?***

  - 화요일에 배운 스크래핑과 코스피지수 데이터 API를 이용하여 주기적으로 알림 **ON**

    ![img](https://lh5.googleusercontent.com/JTCUsVa59EKggYboT77FtE0I32jMA8KDlVSzV_qJ7xoyG6ovOmxZIs2PGtPrplJYloGuD_9YQZ3cu1x3BHyMYQ_BNe44JoBobe2Pkaa0Jd9Te6W_YpwTBrqQQnfyLjB9crWRyllg)

![img](https://lh5.googleusercontent.com/RmfzDI_CHyDk0D1EEgb6A2raTvOiADZ7bW3XbtNHGDic2lTW2u1eNIfEF9El7myfhb6w_DWeLTJsjVT1UElDvse5WhCMHAg0H1RurWQPxzE6MBdg-1J_UanarZ830Md8mfcmS5F5)



