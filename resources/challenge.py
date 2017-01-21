from flask_restful import Resource
from flask_restful import reqparse

challenges = {}


parser = reqparse.RequestParser()
parser.add_argument('id', help='Challenge id')
parser.add_argument('title', help='Challenge title')


class ChallengeList(Resource):
    def get(self):
        # return all challenges
        return challenges
    
    def put(self):
        # adds the challenge to challenges
        #challenges["cha"] = request.form['data']
        args = parser.parse_args()
        challenge = {args['id']: args['title']}
        challenges[args['id']] = challenge
        return challenge, 201

class Challenge(Resource):
    def get(self, challenge_id):
        # return the challenge based on id
        return challenges[challenge_id]

