from flask_restful import Resource
from flask_restful import reqparse, fields, marshal_with
from datetime import datetime
from model import challenge_datasource as datasource
import date_util as dateutil

# marshaller
challenge_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'start_date': fields.DateTime(dt_format='rfc822'),
    'end_date': fields.DateTime(dt_format='rfc822'),
    'days': fields.List(fields.DateTime(dt_format='rfc822'))
}

# request parser
parser = reqparse.RequestParser()
parser.add_argument('title', location = 'json', help = 'Challenge title')
parser.add_argument('start_date', type = lambda x: datetime.strptime(x, '%Y-%m-%d'), location = 'json', help = 'Challenge start date')
parser.add_argument('end_date', type = lambda x: datetime.strptime(x, '%Y-%m-%d'), location = 'json', help = 'Challenge end date')

class Challenges(Resource):
    @marshal_with(challenge_fields, envelope='challenges')
    def get(self):
        # return all challenges
        return datasource.challenges
        
    @marshal_with(challenge_fields, envelope='challenge')
    def post(self):
        args = parser.parse_args()
        id = datasource.get_next_id()
        
        # create challenge object
        if args['start_date'] is not None and args['end_date'] is not None:
            days = dateutil.get_all_dates_between(args['start_date'], args['end_date'])
        else:
            print("days empty")
            days = []
        
        challenge = {
            "id": id, 
            "title": args['title'],
            "start_date": args['start_date'],
            "end_date": args['end_date'],
            "days": days
        }
        
        # add to challenges
        datasource.challenges.append(challenge)
        return challenge, 201
