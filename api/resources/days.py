from flask_restful import Resource
from flask_restful import fields, marshal_with, abort
from datetime import datetime
from model import challenge_datasource as datasource


# marshaller
day_field = {
    'day': fields.DateTime(dt_format='rfc822'),
    'done': fields.Boolean
}
days_fields = {
    'days': fields.List(fields.Nested(day_field))
}

# abort
def abort_if_challenge_doesnt_exist(challenge_id):
    if len([challenge for challenge in datasource.challenges if challenge['id'] == challenge_id]) == 0:
        abort(404, message="Challenge {} doesn't exist".format(challenge_id))

class Days(Resource):

    @marshal_with(days_fields)
    def get(self, challenge_id):
        abort_if_challenge_doesnt_exist(challenge_id)
        the_challenge = [challenge for challenge in datasource.challenges if challenge['id'] == challenge_id]
        return {'days': challenge['days']}