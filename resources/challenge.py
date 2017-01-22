from flask_restful import Resource
from flask_restful import reqparse

challenges = {}
seq = 0

parser = reqparse.RequestParser()
parser.add_argument('title', location='json', help='Challenge title')


def get_id():
    global seq
    seq += 1
    return seq

class ChallengeList(Resource):
    def get(self):
        # return all challenges
        return challenges
    
    def post(self):
        args = parser.parse_args()
        id = get_id()
        challenge = {"id": id, "title": args['title']}
        challenges[id] = challenge
        return challenge, 201

class Challenge(Resource):
    def get(self, challenge_id):
        # return the challenge based on id
        return challenges[challenge_id]

