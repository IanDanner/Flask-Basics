from flask import Flask, render_template, request, redirect, session, flash
import random
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def registration_form():
    return render_template("registration-form.html")

@app.route('/info', methods=['POST'])
def info():
    print "Got Post Info"
    if len(request.form['email']) < 1 or len(request.form['first-name']) < 1 or len(request.form['last-name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm-password']) < 1:
        flash("Field cannot be blank!")
        return redirect('/')
    if any(char.isdigit() for char in request.form['first-name']) == True or any(char.isdigit() for char in request.form['last-name']) == True:
        flash("First/last name must not contain numbers")
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    if len(request.form['password']) < 8:
        flash("Password must be more than 8 characters!")
        return redirect('/')
    if request.form['password'] != request.form['confirm-password']:
        flash("Password does not match Confirm-Password!")
        return redirect('/')
    session['email'] = request.form['email']
    session['first-name'] = request.form['first-name']
    session['last-name'] = request.form['last-name']
    session['password'] = request.form['password']
    flash("Form COMPLETE!")
    return redirect('/')

app.run(debug=True)