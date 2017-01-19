from flask import Flask
from flask_restful import Resource, Api

# Flask app
app = Flask(__name__)

# Api app
api = Api(app)

# HelloWorld
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# add route
api.add_resource(HelloWorld, '/')

# main
if __name__ == '__main__':
    app.run(debug=True)