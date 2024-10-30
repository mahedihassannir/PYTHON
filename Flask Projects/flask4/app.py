from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Home page"


@app.route("/user/<name>")
def person(name):
    return f"{name}"


@app.route("/calculate/<int:num1>/<int:num2>")
def calculation(num1, num2):
    return f"{num1}+{num2}= {num1+num2}"


app = Flask(__name__)


@app.route("/")
def home():
    return "Home page"


@app.route("/user/<name>")
def person(name):
    return f"{name}"


@app.route("/calculate/<int:num1>/<int:num2>")
def calculation(num1, num2):
    return f"{num1}+{num2}= {num1+num2}"


@app.route("/params")
def params():
    if "name" in request.args.keys() and "age" in request.args.keys():
        args = request.args
        age = request.args.get("age")
        return args
    else:
        return "give the required parameters"
