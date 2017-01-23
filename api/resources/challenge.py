from flask_restful import Resource
from flask_restful import reqparse, fields, marshal_with
from datetime import datetime

challenges = {}
seq = 0

parser = reqparse.RequestParser()
parser.add_argument('title', location = 'json', help = 'Challenge title')
parser.add_argument('days', type = int, location = 'json', help = 'Number of days for the challenge')
parser.add_argument('start_date', type = lambda x: datetime.strptime(x, '%Y-%m-%d'), location = 'json', help = 'Challenge start date')

challenge_fields = {
    'title': fields.String,
    'days': fields.Integer,
    'start_date': fields.DateTime(dt_format='rfc822')
}
challenge_list_fields = {
    fields.List(fields.Nested(challenge_fields)),
}

# sequence of ids
def get_id():
    global seq
    seq += 1
    return seq

class Challenges(Resource):
    @marshal_with(challenge_fields, envelope='challenge')
    def get(self):
        # return all challenges
        return challenges
    
    @marshal_with(challenge_fields, envelope='challenge')
    def post(self):
        args = parser.parse_args()
        id = get_id()
        challenge = {"id": id, "title": args['title'], "days": args['days'], "start_date": args['start_date']}
        challenges[id] = challenge
        return challenge, 201

class Challenge(Resource):

    @marshal_with(challenge_fields, envelope='challenge')
    def get(self, challenge_id):
        # return the challenge based on id
        return challenges[challenge_id]
        
    def delete(self, challenge_id):
        #delete the challenge
        del challenges[challenge_id]
        return '', 204

