from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def ColorPicker():
    if 'red' not in session:
        session['red'] = 5
        session['green'] = 120
        session['blue'] = 56
    color = 'style=background-color:rgb('+str(session['red'])+','+str(session['green'])+','+str(session['blue'])+')'
    return render_template("ColorPicker.html", color = color)

@app.route('/colors', methods=['POST'])
def change_color():
    session['red'] = int(request.form['red'])
    session['green'] = int(request.form['green'])
    session['blue'] = int(request.form['blue'])
    return redirect('/')

app.run(debug=True)