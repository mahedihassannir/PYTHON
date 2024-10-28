from flask import Flask
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

app = Flask(__name__)

print(Fore.GREEN + "server is running")


@app.route("/")
def hello_world():
    return "<p>Hello world</p>"
    # return print("Hello world")


@app.route("/products")
def products():
    return "<p>Here is 500 products choose one of them for free</p>"
