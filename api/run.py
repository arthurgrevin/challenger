from flask import Flask
from flask_restful import Api
from resources.challenge import Challenge
from resources.challenges import Challenges
from resources.days import Days
from model.user_model import db
from model.user_model import User


# Flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chalenger.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
#from model.user_model import User

# Api app
api = Api(app)
with app.app_context():
    db.create_all()
    user = User(username="Arthur",email="artae@aekhaze.com")
    session = db.session
    session.add(user)
    print User.query.all()
# add route
api.add_resource(Challenges, '/challenges/')
api.add_resource(Challenge, '/challenges/<int:challenge_id>/')
api.add_resource(Days, '/challenges/<int:challenge_id>/days/')

# main
if __name__ == '__main__':
    app.run(debug=True)