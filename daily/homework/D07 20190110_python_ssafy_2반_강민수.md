### D07 Daily Homework_190110_대전 2반 강민수

### 1. 파이썬은 객체지향 프로그래밍 언어입니다. 파이썬에서 기본적으로 정의된 클래스 5개만 작성해보세요

* ```python
  dict()
  list()
  tuple()
  int()
  set()
  ```

### 2. 다음 중 틀린 것은

* isinstance(인스턴스 객체, 클래스 객체)를 활용하면 상속 관계까지 확인가능하다

### 3. Person 클래스를 정의하고

### 	이름이 '홍길동', 나이가 20인 p1 인스턴스 객체를 만들어보세요.

### 	이름이 ''둘리'' 나이가 0인  p2 인스턴스 객체를 만들어보세요.

```python
class Person:
    def __init__(self, name, age=0): #init의 self는 클래스를 뜻함
        self.name = name
        self.age = age
    def greeting(self):
        print(f'"안녕하세요. {self.name}입니다. {self.age}살 입니다."') # 인스턴스의 self는 인스턴스 p1을 뜻함
        
p1 = Person('홍길동','20')
p1.greeting()
p2 = Person('둘리')
p2.greeting()
```

* 
