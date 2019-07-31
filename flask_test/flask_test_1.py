from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
    return 'Hello %s' % name

# @app.route('/')
# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name=None):
#     if name is None:
#         name = 'World'
#     return 'Hello %s' % name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = eval(request.data)
        print(data)
        return 'This is a POST request'
    else:
        data = request.values.get('data')
        print(data)
        return 'This is a GET request'


url_for('login')    # 返回/login
url_for('login', id='1')    # 将id作为URL参数，返回/login?id=1
url_for('hello', name='man')    # 适配hello函数的name参数，返回/hello/man
# url_for('static', filename='style.css')    # 静态文件地址，返回/static/style.css

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8888, debug=True)
