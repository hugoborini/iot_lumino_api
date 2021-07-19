from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}

