# 웹개발 수업 18.12.17

## #1 개요

### 1. 향후 교육 방향

* Python
* DB
* SQL
* Framework

### 2. 컴퓨터프로그래밍이란?

* 지시사항의 모음
* 명령어의 집합
* 선언형 and 명령형
  * 선언형 : 사실, 정의
  * 명령형 : 방법을 설명, 어렵다
* 퀴즈) 앤퀸즈 > 퇴각 검색
* 프로그래밍의 목적 : 문제를 풀기 위해서

### 3. 4차 산업혁명이란?

* 아디다스 스피드 팩토리 : 100% 로봇 자동화
* Amazon 물류 관리 : 25대의 KIVA로 20만개 물류 처리
* Amazon  드론 배송 : 새로운 개념의 물류 배송. 국내에서는 고층 건물 때문에 무리
* 구글 어시스턴트 : 음성, 챗봇, 인공지능 상용화 단계
* AI 스피커 발전하는 목적 : 최신 트렌드의 인터페이스(스마트폰 > AI 스피커), 데이터 수집
* Amazon이 AI 스피커 글로벌 선두. 전용 언어(알렉사)로 Life Hacking
* YOLO : 영상 디텍팅 비전인식, 딥러닝 기반
* FORBES 2018 Technology Trend : 매년 유망한 기술 트렌드 방향을 짐작해볼 수 있다
* 기술 생산과 기술 활용의 경계가 사라지고 있다
  * 오픈소스로 인프라 공유(ex. AWS)
  * 오픈소스를 조립해서 어플 구성(ex. 카카오톡)
  * 오픈소스를 적극적으로 활용해서 효율적인 SW 개발



## #2 파이썬 기본 실습

### 1. 프로그래밍 언어

* 프로그래밍 3형식 : 저장, 조건(if), 반복(while)
* 대소문자 구분
* 들여쓰기(인덴테이션) 주의
  * 파이썬은 기본 규칙으로 4자 단위 공백
  * 조건과 : 띄우지 않기(ex. if dust > 30:)
  * dust = 60
    * dust에 60을 **넣는다(저장한다, 할당한다)고** 인식하기
  * dust == 60
    * dust는 **60**이라고 인식하기
* Python document의 문법이 기준. 모르면 참고

### 2. 파이썬 문법

* 무엇을 저장하는가
  * 숫자
  * 글자
    * '', ""의 차이는 거의 없다. ""만 가능한 기능이 있다
  * 참/거짓
    * True, False : 첫 글자는 대문자로 해야 참/거짓이 표현된다

* 어떻게 저장하는가
  * 변수
    * 숫자, 글자, 참/거짓을 저장할 수 있음
    * 변수의 모임(ex. 리스트, 튜플)
  * 리스트
    * dust = [1, 2, 3]
  * 딕셔너리
    * 키로 접근해서 Value 값을 출력한다
    * dust = {'영등포':'1'}

* 조건

  * if문

    * ``` if문
      if ~:
      	~~~~
      elif ~:
      	~~~~
      elif ~:
      	~~~~
      else ~:
      	~~~~
      ```

* 반복

  * while문

    * while에 해당할 동안 계속 반복

    * 종료 조건 필수

    * ``` ㄹㄹ
      while ~:
      	~~~~
      ```

  * for문

    * 정해진 범위에서 실행되므로 종료조건 필요없음

    * ``` for in 구문
      for i in dust:
      	print(i)
      ```

* API란

  * 회원가입, 로그인에 사용
  * 서비스와 서비스 간의 대화 방식
  * ex) 공공데이터포털(data.go.kr), Sentiment Analysis
  * 요청 <> 응답

* 함수

  * ```
    변수.함수()
    ```

  * random 함수

    * ![img](https://lh5.googleusercontent.com/K-XKfubVIIQ0cOh377tDvQduM3fDA4fTl7Wl1eEfieL1RYchL-RVSoGgw6SygkFklUtxSMTrn1RTyveXrcU43pwoS3rYSFW7XN1Ay-QPQ6QqnI0G5DRxsUuiLOPcwF4BTrTNz23E)

      * range 함수로 수열을 만들고 List 함수로 리스트 변수를 만든다

        > List 함수를 사용해서 생성, [range()] 불가함, 튜플로 생성 ()

      * random 모듈의 sample 함수로 무작위 숫자를 뽑아낸다

      * sort or sorted 함수로 뽑은 숫자들을 오름차순 배열한다

      * sorted는 원본에 적용되지 않는다

      * print로 출력한다


## #3 CLI 실습

### 1. web browser (Window OS GIT Bash)

1) webbrowser.open(주소)

* python -i : 파이썬 버젼 확인

2) webbrowser.open_new(주소)

3) webbrowser.open_new_tab(주소)



### 2. 정보 스크랩하기

1) 유닉스

> 현대적 컴퓨터 운영체제의 원형(데니스리치)

* darwin. macOS. tvOS, WatchOS, iOS

2) 리눅스

> by 리눅스 토르발스
>
> 클라우드시스템 90%, 스마트폰 80%, 임베디드 60%, 슈퍼컴퓨터 99%
>
> 개발자에게 가장 유리한 OS

* 데비안, 우분투, 구름OS
* 레드헷
* 안드로이드
* 크롬 OS



## #4 GIT 관리

### 1. git, DCVS(distributed Version Control System)

> Server Com <> Computer A,B,C...

* 원본과 수정본의 차이가 무엇이고 수정 이유를 log로 남길 수 있다.
  * 뼈대코드, 메인기능 구현
* 현재 파일들을 안전한 상태로 과거 모습 그대로 복원 가능 (반대도 마찬가지)
  * 메인, 로그인, 채팅기능 구현

### 2. git의 작업flow

> 작업 > 커밋할 목록 > 쌓인 커밋들 > Github

* add : 커밋할 목록에 추가
* commit : 커밋(Create a snapshot) 만들기
* 현재까지의 역사(Commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

### 3. git 기본

* $ git add config --global user.name "kangminsu" : 유저 네임 등록
* $ git add config --global user.email "~~~~@gmail.com" : 유저 이메일 등록
* $ git config --global --list : 작업 확인
* 이후 과정은 수현이가 잘 정리했음!
* push 성공 이후에는 git push만 사용





## #5 for in, if 구문 예제

### 1. 리스트를 한 줄로 출력

![1545033171218](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545033171218.png)

* end='' : 기본적으로 파이썬은 행단위 공백이지만 end를 사용해서 스페이스 공백으로 전환

### 2. 짝수, 홀수 구분하여 리스트에 저장하고 출력 

![1545033089942](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545033089942.png)

* 리스트형 변수(even,odd) 생성한다 : []

* 기본 리스트 numbers 안의 요소 n을 %(나머지 연산)으로 짝,홀수 구분(if문)

* 구분 결과를 even, odd 리스트에 append 함수로 추가한다.

  > even.append(n), odd.append(n)