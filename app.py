from flask import Flask
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return "Hello here is a bunch of functions with Flask endpoint!"

class HelloWorld(Resource):
    def get(self):
        return "Hello World!"

class HelloYou(Resource):
    def get(self, name):        
        return "Hello " + name

class Multiply(Resource):
    def get(self, x, y):        
        x = float(x)
        y = float(y)
        return "Hello " + str(x * y)

class Yell(Resource):
    def get(self, input_text):
        yelled = input_text.upper()
        return yelled

api.add_resource(Home, '/')
api.add_resource(HelloWorld, '/hello-world')
api.add_resource(HelloYou, '/hello/<name>')
api.add_resource(Multiply, '/multiply/<x>/<y>')
api.add_resource(Yell, '/yell-it/<input_text>')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5151, debug=True)