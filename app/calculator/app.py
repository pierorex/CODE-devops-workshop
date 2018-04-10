# encoding=utf-8

from flask import Flask, render_template
from logic import Calculator

app = Flask(__name__)


@app.route("/calc/<a>*<b>")
def multiply(a, b):
    c = Calculator()
    result = c.mul(int(a), int(b))
    return str(result)


@app.route("/calc/<a>/<b>")
def divide(a, b):
    c = Calculator()
    result = c.div(int(a), int(b))
    return str(result)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
