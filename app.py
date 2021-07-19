#import vendor
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
#end import vendor

#import controller
from controller import status as status
#end import controller

app = Flask(__name__)
api = Api(app)
CORS(app)



api.add_resource(status.status, '/')

if __name__ == '__main__':
    app.run()