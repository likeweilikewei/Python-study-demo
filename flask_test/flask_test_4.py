from flask import request, session, Flask, render_template, make_response

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        title = request.args.get('title', 'Default')
        response = make_response(render_template('login.html', title=title), 200)
        response.headers['key'] = 'value'
        return response


from flask import request, session, redirect, url_for


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


app.secret_key = '123456'

if __name__ == '__main__':
    app.run()
