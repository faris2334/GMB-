
from flask import Flask, render_template

app = Flask (min)

@app.route('/')
def home():
    return render_template('t1.html')

if name == 'main':
    app.run(debug=True)