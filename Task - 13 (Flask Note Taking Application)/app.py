from flask import Flask, session, redirect, url_for, escape, request,render_template,flash

app = Flask(__name__)
app.secret_key = 'hello world'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('loggedin.html',username=username)
    return render_template('frontpage.html')


notes=[]
@app.route('/',methods=['POST'])
def note_making():
    if request.form.get("note"):
        n = request.form.get("note")
        notes.append(n)
    return render_template('home.html', notes=notes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    notes.clear()
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template('home.html')
    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
