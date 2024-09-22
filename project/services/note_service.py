from datetime import datetime

import pytz
from flask_restful import abort

from project.repositories.note_repository import NoteRepository
from project.models.note import Note

class NoteService:
    def __init__(self):
        self.repository = NoteRepository()

    def get_all_notes(self):
        return self.repository.get_all_active()

    def get_note_by_id(self, note_id):
        note = self.repository.get_by_id(note_id)
        if note is None:
             abort(404, message="Note not found")
        return note

    def create_note(self, heading, body):
        note = Note(heading=heading, body=body)
        self.repository.add(note)
        return note

    def update_note(self, note_id, heading, body):
        note = self.repository.get_by_id(note_id)
        if note is None:
             abort(404, message="Note not found")
        note.heading = heading
        note.body = body
        self.repository.update(note)
        return note

    def delete_note(self, note_id):
        note = self.repository.get_by_id(note_id)
        if note is None:
            abort(404, message="Note not found")

        note.deleted_at = datetime.now(pytz.utc)  # Use UTC for consistency
        note.active = False
        self.repository.update(note)

        return self.repository.get_all_active()
