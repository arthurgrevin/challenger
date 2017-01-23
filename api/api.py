from flask import Flask
from flask_restful import Api
from resources.challenge import Challenge, Challenges

# Flask app
app = Flask(__name__)

# Api app
api = Api(app)

# add route
api.add_resource(Challenges, '/challenges/')
api.add_resource(Challenge, '/challenges/<int:challenge_id>')

# main
if __name__ == '__main__':
    app.run(debug=True)