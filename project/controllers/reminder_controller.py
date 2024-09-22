from project.services.reminder_service import ReminderService

class ReminderController:
    def __init__(self):
        self.service = ReminderService()

    def get_reminders(self):
        return self.service.get_all_reminders()

    def create_reminder(self, email, note_id, reminder_date):
        return self.service.create_reminder(email, note_id, reminder_date)