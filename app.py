from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
   message = 'Добро пожаловать!'
   return render_template('index.html', message=message)
