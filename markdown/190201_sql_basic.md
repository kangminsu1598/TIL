### C9에서 flask 사용

#### 가상환경 만들기

* c9 setting

  ```txt
  # install pyenv
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.6.7
  pyenv global 3.6.7
  pyenv rehash
  
  
  # install pyenv-virtualenv
  git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
  source ~/.bashrc
  
  
  # etc
  python -V
  pip install -U pip
  pip install flask
  pip install requests
  pip freeze > req.txt
  ```


#### 플라스크 데이터 request

```python
from flask import Flask, render_template

import os
import datetime

@app.route("/ping_new")
def ping_new():
    return render_template('ping_new.html')
    
@app.route("/pong_new", methods=['POST'])
def pong_new():
    name = request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)

# op.gg
@app.route("/opgg")
def opgg():
    return render_template('opgg.html')
        
@app.route("/opgg_result")
def opgg_result():
    url = "http://www.op.gg/summoner/userName="
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    
    return render_template('opgg_result.html', username = username, wins=wins.text)

# CSV
@app.route('/timeline')
def timeline():
    # 지금까지 기록되어 있는 방명록들을 보여주자!
    my_list = []
    with open('timeline.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            my_list.append(row)
    
    return render_template('timeline.html', my_list=my_list)
    
@app.route('/timeline_create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    with open('timeline.csv', 'a', newline='') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # 이 문장과 같음. writer = csv.DictWriter(f, fieldnames=['username','massage'])
        writer.writerow({
            'username': username,
            'message' : message
        })
    
    return redirect('/timeline')
    # return render_template('timeline_create.html', username=username, message=message)




# c9이 연 아이피를 호스팅한다, 포트 찾는다, 디버그 실시간으로 한다.
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

```html
# 반복문, 조건문    

	{% if name2 == '강민수' %}
    <h1>hello, {{ name2 }}</h1>
    {% else %}
    <h2>너 누구야</h2>
    {% endif %}

	{% for movie in movies %}
	<li>{{ movie }}</li>
	{% endfor %}
```

#### 데이터베이스(DB)

* RDBMS
* 관계형 데이터베이스

  * SQLite! 배운다!

* 용어 정리

  * 스키마: 데이터 구분

* sqlite flow (테이블 생성)

  * .mode csv

  * dd

  * dd

  * 쿼리문 SELECT * FROM 표이름;

    * SELECT : 특정 데이터를 반환 함

    * 쿼리문에서만 ;으로 마무리 함

* 명령어

  * .tables
  * .schema
  * .headers on
  * .mode column
  * DROP TABLE classmate;

* 데이터 편집(생성, 보기, 수정, 삭제)

  * INSERT INTO classmate

    * ```sql
      INSERT INTO classmate (name, age, address)
      VALUES('안상현', 23, '대전');
      INSERT INTO classmate (name, age, address)
      VALUES('신채원', 23, '서울');
      ```

  * SELECT *  FROM classmate

    * ```sql
      -- 테이블 값 모두 가져오기
      SELECT * FROM classmate;
      -- 테이블의 특정 컬럼만 가져오기
      SELECT id, name FROM classmate;
      -- 가져오는 ROW(레코드) 개수를 지정하기
      SELECT id, name FROM classmate LIMIT 2;
      -- LIMIT OFFSET 세트로 쓰임. 리미트 ROW 부터 offset 떨어진 ROW를 지정
      SELECT * FROM classmate LIMIT 1 OFFSET 2;
      -- 특정 값을 가진 ROW만 지정
      SELECT * FROM classmate WHERE address='서울';
      ```

  * UPDATE classmate

    * ```sql
      -- 테이블을 수정한다
      UPDATE classmate
      SET name='박성주', address='제주'
      WHERE id=4 or id=6;
      ```

  * DELETE classmate

    * ```sql
      -- 보통 값을 지울 때는 유니크한 값인 ID를 지운다.
      DELETE FROM classmate WHERE id=3;
      -- 지운 아이디는 다른 값으로 갱신되지 않는다.
      ```