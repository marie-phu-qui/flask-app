from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'hellos'},
    'todo2': {'task': 'multiply'},
    'todo3': {'task': 'yell stuff'},
}

class Home(Resource):
    def get(self):
        return "Hello Hello here is a bunch of functions with Flask endpoint!"

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

class Post(Resource):
    def get(self):
        number = float(request.args.get('number'))
        number_squared = number ** 2
        return "{} ^ 2 = {}".format(number, number_squared)
    def post(self):
        req_data = request.get_json(force=True)
        number = req_data["number"]
        number_squared = number ** 2
        return "Methode post : {} ^ 2 = {}".format(number, number_squared)

        

api.add_resource(Home, '/')
api.add_resource(HelloWorld, '/hello-world')
api.add_resource(HelloYou, '/hello/<name>')
api.add_resource(Multiply, '/multiply/<x>/<y>')
api.add_resource(Yell, '/yell-it/<input_text>')
api.add_resource(Post, '/post')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5151, debug=True)