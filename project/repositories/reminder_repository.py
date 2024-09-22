from project.models.reminder import Reminder
from project.db import db

class ReminderRepository:
    def get_all(self):
        return Reminder.query.all()

    def get(self, id):
        return Reminder.query.get(id)

    def add(self, reminder):
        db.session.add(reminder)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, reminder):
        db.session.delete(reminder)
        db.session.commit()
