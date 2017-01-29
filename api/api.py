from flask import Flask
from flask_restful import Api
from resources.challenge import Challenge, Challenges, Days

# Flask app
app = Flask(__name__)

# Api app
api = Api(app)

# add route
api.add_resource(Challenges, '/challenges/')
api.add_resource(Challenge, '/challenges/<int:challenge_id>')
api.add_resource(Days, '/challenges/<int:challenge_id>/days/')

# main
if __name__ == '__main__':
    app.run(debug=True)