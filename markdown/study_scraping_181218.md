# Web의 구조와 Web 스크래핑

## Session #1 ...?

> ublock origin 
>
> momentum : 화면보호기
>
> Visual Studio > thema 검색 > material
>
> V/S
>
> * 저장 : Ctrl + S
> * 주석처리 : ctrl + /
>
> CLI
>
> * 파일 생성 : touch > ex) touch string_test
>
> * CLI 화면 올리기 : ctrl + L
>
> * CLI 파일명 : 일정 부분 치고 TAB 사용하면 자동 완성
>
> * CLI로 파일 열기 : code 파일명
>
> * CLI로 내용 확인 : cat 파일명
>
> **for문 작업 시 list 말고 range 사용해야 메모리 최소화**
>
> * **range는 메모리 1칸, list는 내용만큼 칸수 늘어남**
>
> from ~ import ~ as
>
> * from : 큰 패키지 지칭
> * import : 함수 들여오기
> * as : 함수 이름 변경
>
> strip 메소드
>
> * 변수.strip() : 전체 공백 삭제
> * lstrip() : 왼쪽 공백 삭제
>
> * rstrip() : 오른쪽 공백 삭제
>
> GIT
>
> * git add : 커밋에 반영
> * git status : 깃 상태 보기
> * git commit - m '커밋 이름' : 커밋 추가
> * ls -al : 모든 git 폴더 확인
> * rm -rf 폴더.git : 잘못된 폴더 삭제



### 1. String 메소드 사용법

1) 파이썬 과거

```
%s, %s % ('변수', '변수')
```

* ex) print('일은 영어로 %s, 이는 영어로 %s' % ('one', 'two'))

2) pyformat 

```py
{} {}.format('변수', '변수')
```

* ex) print(''일은 영어로{} 이는 영어로{}''.format('one', 'two'))

3) f-string python 3.6

```
f~~~{변수} ~~~~{변수}
```

* f가 f-string을 의미한다
* f 다음에 인덴테이션 안해야 메소드로 인식된다

4) 간략화

```simp
+ 변수 +
```

* ex) print("'안녕하세요'+ name + '입니다")



### 2. 파일명 바꾸기

1) OS를 import한다

```
import os
```

2) 해당 폴더로 들어간다

```
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
```

* os.chdir에서 폴더명이 사용됐기 때문에 "."으로 표현
* window에서 사용할 때 주소 앞에 r을 추가하고 작성

3) 폴더 안에 모든파일을 돌면서 이름을 바꾼다

```renam
for filename in os.listdir('.'):
	os.rename(filename, filename.replace('SAMSUNG','SSAFY')
```

4) 명령어

* os.chdir(r'폴더주소')
  * 작업하고 있는 위치 변경

* os.listdir('폴더주소')
  * 지정된 디렉토리 전체 파일 목록 얻기
  * 변수는 단수 이름으로 정하기 (ex) filename)

* os.rename(변수, 변수.replace())
  * 변수. replace(현재파일명, 바꿀 파일명)



### 3. 파일 수정

```
f = open('파일명.확장자','작업종류','인코딩)
```

* 파일이 없으면 생성하면서 파일을 연다

2) 작업(작성, 추가, 읽기)한다

```
변수명.작업종류()
```

* 작업 메소드

  * write : 내용 작성, 덮어 쓰기
  * writelines : 여러줄 작성
  * read : 파일 읽기
  * readline : 한줄씩 읽기, 한 줄 출력
  * readlines : 여러줄 읽기, 파일 전체를 리스트 형태로 출력

  ![img](https://lh3.googleusercontent.com/2oFUck2-N5ktcUI0vBQ2SqNak15a2pewZ_68agfzohZ9SXEQb3V_dLgwNY1Y8Ukqvfpe1w1EIWUdZTkWG5Z4577a5znahzbaTA7E_FTJFcXRYMT6LgXqNYbltEFjIxCgolGNXkSH)

  * append : 내용 추가

3) 닫는다

```
변수명.close
```

* **with as 구문 사용하면 쓸 필요 없음**

* 작업 메소드
  * close

4) 간략화 (with as 구문)

```
with open('파일명','작업종류') as f(파일 여는 변수임):
	f.작업종류(작업 대상이 되는 변수명)
```

* **as f 이후 : 빠뜨리지 않기!**



## # 용어정리

### 1. 함수

* 매개변수의 자리가 상수로 특정되면 인수라고 한다

### 2. 클래스

### 3. 메소드



## Session #2. 정보 찾기

### 1. 정보스크랩

> 웹과 정보 주고 받는 목적

* 명령어
  * requests.get(''주소'') : 주소에 요청을 보내서 정보를 받아옴
  * requests.get("주소").text
  * requests.get("주소").status_code : 리퀘스트 상태
  * beuatifulsoup : 문서를 이쁘게 꾸며주는 함수
  * .select_one : 문서 안의 특정 내용 하나를 뽑는 메소드
  *  .select : 문서 안에 있는 특정 내용을 뽑는 메소드
    * readlines처럼 전체 내용을 긁는 데 사용되고, 이후 for 문에서 select one을 사용해서                 하나씩 반복한다.

* 정보스크랩 1단계

  1) 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다

  2) BeautifulSoup 메소드로 응답의 가독성을 높인다

  3) 정보를 출력하여 확인한다

  * 화살표는 직속 자식, 자식의 자식...이면 스페이스바로 하위 개념 표시
  * 스페이스로 클래스를 구분한다

