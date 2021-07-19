#import vendor
from flask import Flask, jsonify, jsonify, request
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
#end import vendor

#import controller
from controller import status, getAllRoom, bookARoom, getAllBookingFromARoom
#end import controller



app = Flask(__name__)
api = Api(app)
CORS(app)

# declare all api route
api.add_resource(status.status, '/')
api.add_resource(getAllRoom.getAllRoom, '/getAllRoom')
api.add_resource(bookARoom.bookARoom, '/bookaroom')
api.add_resource(getAllBookingFromARoom.getAllBookingFromARoom, '/getAllBookingFromARoom/<string:nameRoom>')
# end declare all api route

if __name__ == '__main__':
    app.run()