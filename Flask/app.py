from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return '안녕하세요'

@app.route('/chic')
def html():
    return render_template('chicken.html')

@app.route('/html_name/<string:name>')
def html_name(name):
    return render_template('chicken.html', your_name = name)
# chicken.html 페이지를 띄워주세요

@app.route('/dictionary/<string:word>')
def dictionary(word):
    word_dict = {'banana':'바나나','apple':'사과'}
    return render_template('word.html', word = word, word_dict = word_dict)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, dubug=True)