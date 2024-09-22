from project.models.note import Note
from project.db import db

class NoteRepository:
    def get_all(self):
        return Note.query.all()

    def get_all_active(self):
        return Note.query.filter(Note.active == True).all()

    def get_by_id(self, note_id):
        return Note.query.get(note_id)

    def add(self, note):
        db.session.add(note)
        db.session.commit()

    def update(self, note):
        db.session.commit()

    def delete(self, note):
        db.session.delete(note)
        db.session.commit()
