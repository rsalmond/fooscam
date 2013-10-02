from flask import Flask, jsonify
from flask.ext.restful import Api, Resource, reqparse
from flask import abort

import json

import pdb

app = Flask(__name__)
api = Api(app)

class Score(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('score', type = dict, required = True, help = 'No score data provided', location = 'json')
        super(Score, self).__init__()

    def get(self):
        pass

    def post(self):
        args = self.reqparse.parse_args()
        try:
            red_score = args['score']['red']
            blue_score = args['score']['blue']
        except KeyError:
            return {'status': 'invalid JSON data'}, 400

        return {'status': 'accepted'}, 201

class Players(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('team', type = list, required = True, help = 'No team data provided', location = 'json')
        super(Players, self).__init__()

    def get(self):
        pass

    def post(self):
        args = self.reqparse.parse_args()
        if len(args['team']) == 2:
            try:
                blue_off = args['team'][0]['blue']['offense']
                blue_def = args['team'][0]['blue']['defense']
                red_off = args['team'][1]['red']['offense']
                red_def = args['team'][1]['red']['defense']
            except (KeyError, IndexError):
                return {'status': 'invalid JSON data'}, 400
            return {'status': 'accepted'}, 201
        else:
            return {'status': 'invalid JSON data (only TWO teams in foosball!)'}, 400

api.add_resource(Score, '/score', endpoint = 'score')
api.add_resource(Players, '/players', endpoint = 'players')

if __name__ == '__main__':
    app.run(debug=True)
