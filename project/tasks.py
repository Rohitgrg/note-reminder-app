from math import trunc

import pytz
from datetime import datetime, timedelta

from celery import shared_task
from project.services.note_service import NoteService
from project.services.email_service import EmailService

email_service = EmailService()
note_service = NoteService()

@shared_task
def send_email_task(email, note_id, reminder_id):
    from project.services.reminder_service import ReminderService
    reminder_service = ReminderService()

    try:
        print('Sending email', email, note_id)
        note = note_service.get_note_by_id(note_id)
        if not note.active:
            subject = "Note reminder for " + note.heading
            email_body = "Your Note says: " + note.body
            email_service.send_email(email, subject, email_body)
            reminder_service.set_reminder_status(reminder_id)
            print("Email sent to {}".format(email))
    except Exception as e:
        print("Email sending failed: {}".format(e))

@shared_task
def check_reminders_task():
    from project.services.reminder_service import ReminderService
    reminder_service = ReminderService()

    print("Checking reminders...")

    reminders = reminder_service.get_all_reminders()
    current_time_utc = datetime.now(pytz.utc)
    one_hour_from_now_utc = current_time_utc + timedelta(hours=1)

    for reminder in reminders:
        target_datetime_local = reminder.reminder_date
        target_datetime_utc = target_datetime_local.astimezone(pytz.utc)

        if target_datetime_utc <= one_hour_from_now_utc and not reminder.sent:
            send_email_task.apply_async(args=(reminder.email, reminder.note_id, reminder.id), eta=target_datetime_utc)
            print(f"Task scheduled for reminder {reminder.id} at {target_datetime_utc}")

    print("Finished checking reminders.")