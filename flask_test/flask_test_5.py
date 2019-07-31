from flask import request, session, make_response, Flask, redirect, url_for, render_template
import time

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])  # 用装饰器生成URL和视图函数的映射
def login():  # 视图函数
    response = None
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            return 'No such user!'
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            title = request.args.get('title', 'Default')
            response = make_response(render_template('login.html', title=title), 200)
            response.headers['key'] = 'value'
            return response
    return response

app.secret_key = '123456'


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


from flask import session, redirect


@app.route('/')
def index():
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        return redirect(url_for('login'), 302)


from flask import abort


@app.route('/error')
def error():
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
