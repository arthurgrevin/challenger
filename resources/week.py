from flask_restful import Resource
from flask import request

weeks = {}

class Week(Resource):
    def get(self):
        # return all weeks
        return weeks

class WeekSimple(Resource):
    def get(self, week_id):
        # return the week based on id
        return {week_id: weeks[week_id]}

    def put(self, week_id):
        # adds the week to weeks
        weeks[week_id] = request.form['data']
        return {week_id: weeks[week_id]}

