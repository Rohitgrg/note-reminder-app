from flask_restful import Resource, fields, marshal_with, reqparse
from project.controllers.note_controller import NoteController

note_parser = reqparse.RequestParser()
note_parser.add_argument('body', type=str, required=True)
note_parser.add_argument('heading', type=str, required=True)

note_controller = NoteController()

note_dto = {
    'id': fields.Integer,
    'heading': fields.String,
    'body': fields.String
}

class NoteList(Resource):
    @marshal_with(note_dto)
    def get(self):
        return note_controller.get_notes()

    @marshal_with(note_dto)
    def post(self):
        data = note_parser.parse_args()
        return note_controller.create_note( data['heading'], data['body'])

class NoteResource(Resource):
    @marshal_with(note_dto)
    def get(self, pk):
        return note_controller.get_note(pk)

    @marshal_with(note_dto)
    def put(self, pk):
        data = note_parser.parse_args()
        return note_controller.update_note(pk, data['heading'], data['body'])

    @marshal_with(note_dto)
    def delete(self, pk):
        return note_controller.delete_note(pk)

notes_api = NoteList
note_api = NoteResource
