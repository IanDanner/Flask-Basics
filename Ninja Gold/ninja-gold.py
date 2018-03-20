from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def activity(gold,action,place):
    timestamp = datetime.datetime.now()
    if place == 'casino':
        if action == 'collect':
            collect = "Entered a casino and won %d golds, you have great LUCK! %s" % (gold, timestamp)
            session['activity'].append(['collect', collect])
        elif action == 'lose':
            lost = "Entered a casino and lost %d golds...... what terrible LUCK... %s" % (gold, timestamp)
            session['activity'].append(['lose', lost])
    elif place == 'farm':
        session['activity'].append(['collect', "Earned %d golds from the farm! %s" % (gold, timestamp)])
    elif place == 'cave':
        session['activity'].append(['collect', "Earned %d golds from the cave! %s" % (gold, timestamp)])
    elif place == 'house':
        session['activity'].append(['collect', "Earned %d golds from the house! %s" % (gold, timestamp)])

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activity'] = []
    return render_template("ninja-gold.html", activities = session['activity'])

@app.route('/process_money', methods=['POST'])
def process_money():
    session['money'] = request.form['money']
    if session['money'] == 'farm':
        rand1 = random.randint(10,20)
        session['gold'] += rand1
        activity(rand1, 'collect', 'farm')
    elif session['money'] == 'cave':
        rand1 = random.randint(5,10)
        session['gold'] += rand1
        activity(rand1, 'collect', 'cave')
    elif session['money'] == 'house':
        rand1 = random.randint(2,5)
        session['gold'] += rand1
        activity(rand1, 'collect', 'house')
    elif session['money'] == 'casino':
        rand1 = random.randint(0,20)
        rand2 = random.randint(0,1)
        if rand2 == 0:
            session['gold'] += rand1
            activity(rand1, 'collect', 'casino')
        elif rand2 == 1:
            session['gold'] -= rand1
            activity(rand1, 'lose', 'casino')
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['activity'] = []
    return redirect('/')

app.run(debug=True)