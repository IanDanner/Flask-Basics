from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'random' not in session:
        session['random'] = random.randint(1,100)
        print session['random']
        guess = ""
    if 'guess' in session:
        if session['guess'] == session['random']:
            guess = "Correct "+str(session['random'])+" was the Number"
        elif session['guess'] > session['random']:
            guess = "You are to High"
        elif session['guess'] < session['random']:
            guess = "You are to Low"
    return render_template("great-number-game.html", guess = guess)

@app.route('/guess', methods=['POST'])
def guess():
    print "something"
    num = request.form['num']
    session['guess'] = int(num)
    print session['guess']
    return redirect('/')

@app.route('/reroll', methods=['POST'])
def reroll():
    session.pop('random')
    session.pop('guess')
    return redirect('/')

app.run(debug=True)
