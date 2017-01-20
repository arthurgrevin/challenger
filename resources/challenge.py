from flask_restful import Resource
from flask import request

challenges = {}

class Challenge(Resource):
    def get(self):
        # return all challenges
        return challenges

class ChallengeSimple(Resource):
    def get(self, challenge_id):
        # return the challenge based on id
        return {challenge_id: challenges[challenge_id]}

    def put(self, challenge_id):
        # adds the challenge to challenges
        challenges[challenge_id] = request.form['data']
        return {challenge_id: challenges[challenge_id]}

