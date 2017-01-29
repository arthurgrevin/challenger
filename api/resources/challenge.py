from flask_restful import Resource
from flask_restful import reqparse, fields, marshal_with, abort
from datetime import datetime

challenges = []
seq = 0

parser = reqparse.RequestParser()
parser.add_argument('title', location = 'json', help = 'Challenge title')
parser.add_argument('nb_days', type = int, location = 'json', help = 'Number of days for the challenge')
parser.add_argument('start_date', type = lambda x: datetime.strptime(x, '%Y-%m-%d'), location = 'json', help = 'Challenge start date')
parser.add_argument('end_date', type = lambda x: datetime.strptime(x, '%Y-%m-%d'), location = 'json', help = 'Challenge end date')

# marshaller
challenge_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'nb_days': fields.Integer,
    'start_date': fields.DateTime(dt_format='rfc822'),
    'end_date': fields.DateTime(dt_format='rfc822')
}
    
challenge_list_fields = {
    fields.List(fields.Nested(challenge_fields)),
}


# sequence of ids
def get_next_id():
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
        id = get_next_id()
        
        # create challenge object
        challenge = {
            "id": id, 
            "title": args['title'], 
            "nb_days": args['nb_days'], 
            "start_date": args['start_date'],
            "end_date": args['end_date']
        }
        
        # add to challenges
        challenges.append(challenge)
        return challenge, 201


def abort_if_challenge_doesnt_exist(challenge_id):
    if len([challenge for challenge in challenges if challenge['id'] == challenge_id]) == 0:
        abort(404, message="Challenge {} doesn't exist".format(challenge_id))


class Challenge(Resource):
    @marshal_with(challenge_fields, envelope='challenge')
    def get(self, challenge_id):
        # return the challenge based on id
        abort_if_challenge_doesnt_exist(challenge_id)
        return [challenge for challenge in challenges if challenge['id'] == challenge_id]
        
    def delete(self, challenge_id):
        # delete the challenge
        abort_if_challenge_doesnt_exist(challenge_id)
        for challenge in challenges[:]:
            if challenge['id'] == challenge_id:
                # do something with item
                challenges.remove(challenge)
        return '', 204

