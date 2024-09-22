from datetime import datetime

from flask_restful import Resource, fields, marshal_with, reqparse
from project.controllers.reminder_controller import ReminderController

reminder_parser = reqparse.RequestParser()
reminder_parser.add_argument('note_id', type=int, required=True)
reminder_parser.add_argument('reminder_date', type=str, required=True)
reminder_parser.add_argument('email', type=str, required=True)

reminder_controller = ReminderController()

reminder_dto = {
    'id': fields.String,
    'note_id': fields.Integer,
    'reminder_date': fields.DateTime,
}

class Reminder(Resource):
    @marshal_with(reminder_dto)
    def get(self):
        return reminder_controller.get_reminders()

    @marshal_with(reminder_dto)
    def post(self):
        data = reminder_parser.parse_args()
        return reminder_controller.create_reminder(data['email'], data['note_id'], data['reminder_date'] )

reminder_api = Reminder
