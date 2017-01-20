from flask import Flask
from flask_restful import Api
from resources.challenge import Challenge
from resources.challenge import ChallengeSimple

# Flask app
app = Flask(__name__)

# Api app
api = Api(app)

# add route
api.add_resource(Challenge, '/challenges/')
api.add_resource(ChallengeSimple, '/challenges/<string:challenge_id>')

# main
if __name__ == '__main__':
    app.run(debug=True)