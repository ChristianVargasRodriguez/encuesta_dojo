from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'Patata_33'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comments=session['comments'])


if __name__ == '__main__':
    app.run(debug=True)