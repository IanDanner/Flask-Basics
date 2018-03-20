from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def counter():
    session['count'] += 1
    return render_template('Counter.html', count = session['count'])

@app.route('/add', methods=['POST'])
def add():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)