import uuid
from datetime import datetime, timedelta, timezone
import pytz

from project.models.reminder import Reminder
from project.repositories import ReminderRepository
from project.tasks import send_email_task


class ReminderService:
    def __init__(self):
        self.repository = ReminderRepository()

    def get_all_reminders(self):
        return self.repository.get_all()

    def set_reminder_status(self, reminder_id):
        reminder = self.repository.get(reminder_id)
        reminder.sent = True
        self.repository.update()

    def create_reminder(self, email, note_id, reminder_date):
        new_reminder_id = str(uuid.uuid4())
        reminder = Reminder(id=new_reminder_id, note_id=note_id, reminder_date=reminder_date, email=email)
        self.repository.add(reminder)
        target_datetime = datetime.fromisoformat(reminder_date).astimezone(pytz.utc)
        current_time = datetime.now().astimezone(pytz.utc)
        one_hour_from_now = current_time + timedelta(hours=1)
        if target_datetime < one_hour_from_now:
            task = send_email_task.apply_async(args=(email, note_id, new_reminder_id), eta=target_datetime)
        return reminder

