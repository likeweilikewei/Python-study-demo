from flask import render_template, request, session, url_for, redirect, flash, Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    if 'user' in session:
        return render_template('hello.html', name=session['user'])
    else:
        return redirect(url_for('login'), 302)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            flash('Login successfully!', 'message')
            flash('Login as user: %s.' % request.form['user'], 'info')
            return redirect(url_for('index'))
            # return jsonify({'likewei': 'iloveu', 'ResponCode': '000', 'ResponMessage': '收到请求'})
    else:
        return '''
        <form name="login" action="/login" method="post">
            Username: <input type="text" name="user" />
        </form>
        '''

app.secret_key = '123456'

if __name__ == '__main__':
    app.run()
