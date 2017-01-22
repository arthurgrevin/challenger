from flask_restful import Resource
from flask_restful import reqparse

challenges = {}


parser = reqparse.RequestParser()
parser.add_argument('id', location='json', help='Challenge id')
parser.add_argument('title', location='json', help='Challenge title')


class ChallengeList(Resource):
    def get(self):
        # return all challenges
        return challenges
    
    def post(self):
        args = parser.parse_args()
        challenge = {"id": args['id'], "title": args['title']}
        challenges[args['id']] = challenge
        return challenge, 201

class Challenge(Resource):
    def get(self, challenge_id):
        # return the challenge based on id
        return challenges[challenge_id]

