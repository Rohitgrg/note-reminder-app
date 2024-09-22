from flask_restful import Resource, abort

class CustomError(Resource):
    def get(self):
        abort(400, message="The request was invalid.")