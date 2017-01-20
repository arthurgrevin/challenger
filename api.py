from flask import Flask
from flask_restful import Api
from resources.week import Week
from resources.week import WeekSimple

# Flask app
app = Flask(__name__)

# Api app
api = Api(app)

# add route
api.add_resource(Week, '/weeks/')
api.add_resource(WeekSimple, '/weeks/<string:week_id>')

# main
if __name__ == '__main__':
    app.run(debug=True)