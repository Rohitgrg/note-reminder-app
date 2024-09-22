from project.services.note_service import NoteService

class NoteController:
    def __init__(self):
        self.service = NoteService()

    def get_notes(self):
        return self.service.get_all_notes()

    def get_note(self, note_id):
        return self.service.get_note_by_id(note_id)

    def create_note(self, heading, body):
        return self.service.create_note(heading, body)

    def update_note(self, note_id, heading, body):
        return self.service.update_note(note_id, heading, body)

    def delete_note(self, note_id):
        return self.service.delete_note(note_id)
