# encoding=utf-8

from flask import Flask, render_template
from calculator.logic import Calculator
from calculator.logic import ValueTooLowException, ValueTooHighException

app = Flask(__name__)


@app.route("/calc/<a>*<b>")
def multiply(a, b):
    c = Calculator()
    try:
        result = c.mul(int(a), int(b))
    except ValueTooLowException:
        return 'Value too low', 403
    except ValueTooHighException:
        return 'Value too high', 403
    return str(result)


@app.route("/calc/<a>/<b>")
def divide(a, b):
    c = Calculator()
    try:
        result = c.div(int(a), int(b))
    except ZeroDivisionError:
        return 'Division by 0', 403
    except ValueTooLowException:
        return 'Value too low', 403
    except ValueTooHighException:
        return 'Value too high', 403
    return str(result)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
