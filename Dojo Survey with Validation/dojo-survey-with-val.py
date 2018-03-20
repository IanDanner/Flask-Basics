from flask import Flask, render_template, request, redirect, session, flash
import random
import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def dojo_survey():
    return render_template("dojo-survey-with-val.html")

@app.route('/results', methods=['POST'])
def results():
    print "Got Post Info"
    if len(request.form['name']) < 1 or len(request.form['comment']) < 1:
        flash("Name/Comment cannot be blank!")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comment cannot be longer than 120 characters")
        return redirect('/')
    elif len(request.form['name']) > 1 or len(request.form['comment']) >1:
        session['name'] = request.form['name']
        session['comment'] = request.form['comment']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    
    return render_template("dojo-survey-result.html")

app.run(debug=True)