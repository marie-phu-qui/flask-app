from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello here is a bunch of functions with Flask endpoint!"

@app.route('/hello/<username>', methods=['GET'])
def login(username):
    return "hello " + username

@app.route("/multiply/<number>/<multiplier>")
def gryshka(number, multiplier):
    return "Your {} * {} is {}".format(number, multiplier, float(number) * float(multiplier))


# @app.route("/subtract/<number>/<subtract>")
# def subtract():
#     result = number - subtract
#     return "Hello subtract!"+ result

# @app.route("/add")
# def add():
#     return "Hello addition!"

# @app.route("/divide")
# def divide():
#     return "Hello divide!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5151, debug=True)