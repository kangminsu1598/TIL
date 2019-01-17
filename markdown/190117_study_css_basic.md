## css

### box model

#### 1. 구조

margin

border

padding

context

#### 2. 태그 구분

block : 개행됨

* div

inline : 문장 중간에 들어갈 수 있음

* span, a, strong, img, br, input, select, textarea, button

inline-block: 한줄에 표시되면서 block처럼 크기 조절(width, height, margin(top, bottom))이 가능하다.

* inline을 inline-block으로 속성을 바꿔서 사용한다

None : 해당 요소를 화면에 표시하지 않는다.

* **공간까지 사라진다**

visibility Property

* visible : 디폴트 값
* hidden 해동 요소를 안보이게 한다.
  * **공간은 존재한다**



### 포지션

#### static

* 기본값

#### relative

* 기본 위치를 기준으로 프롬프트를 사용해서 상대적으로 위치를 이동
* position 적용 전(static) 기준으로 움직임. **움직인 후 원래 있던 공간도 객체가 차지하고 있다..**

#### absolute

* 기본 레이어 관계에서 벗어난다.

* **움직인 후 원래 있었던 공간은 더이상 차지하지 않는다.**

* **즉, 다른 도형들도 새로운 자리로 움직이게 된다.**

* 부모 영역을 벗어나 어디든 자유롭게 위치할 수 있다.

  >  TIP. 부모에게 position: relative를 줘서 자식이 absolute를 받을 때 기준점을 부모로 인식하도록 하는 것이 편하다.

* 부모에 static 이외에 position 프로퍼티가 지정되어 있을 경우에만 부모를 기준으로 위치하게 된다. 만약 부모 조상이 모두 static이면 document body를 기준으로 위치하게 된다.

#### fixed

* absolute와 동일하게 움직이지만 스크롤이 생길 때 움직이지 않고 고정되어 있다.

#### nth-child(n)

* 모든 자식의 순서에서 찾음
* 해당하는 태그의 순서

#### nth-of-type(n)

* 해당하는 자식 태그 요소의 순서를 찾음
* 특정 자식의 속성을 찾음. 

ssafy 아이디의 모든 자식 중 2번째

nth of type은 p 태그 중에 2개

