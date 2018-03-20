from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def DisappearingNinja():
    return render_template("DisappearingNinja.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def ninjaColor(color):
    if color == 'blue':
        return render_template("leonardo.html")
    if color == 'orange':
        return render_template("michelangelo.html")
    if color == 'red':
        return render_template("raphael.html")
    if color == 'purple':
        return render_template("donatello.html")
    else:
        return render_template("notapril.html")

app.run(debug=True)