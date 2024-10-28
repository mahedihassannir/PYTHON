from flask import Flask, render_template, request, jsonify
from colorama import Fore, init

init(autoreset=True)

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def root():
    return "Hello World"


@app.route("/product")
def all_products():
    return "<h1>ALL PRODUCT ARE HERE</h1>"


@app.route("/user/<name>")
def all(name):
    return "<h1>MY NAME IS {}!!!</h1>".format(name)


@app.route("/api/v1/auth/login", methods=["POST"])
def login():

    data = request.get_json()
    print(data)

    return jsonify({"message": "login successfully completed"}), 201


@app.errorhandler(404)
def not_found(e):
    return "not found 404", 404
