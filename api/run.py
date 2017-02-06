from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.challenge import Challenge
from resources.challenges import Challenges
from resources.days import Days

# Flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////projects/challenger.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#from model.user_model import User

# Api app
api = Api(app)

# add route
api.add_resource(Challenges, '/challenges/')
api.add_resource(Challenge, '/challenges/<int:challenge_id>/')
api.add_resource(Days, '/challenges/<int:challenge_id>/days/')

# main
if __name__ == '__main__':
    app.run(debug=True)