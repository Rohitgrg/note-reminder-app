import uuid
from datetime import datetime, timezone

from project.db import db

class Reminder(db.Model):
    id = db.Column(db.UUID(as_uuid=True) , primary_key=True)
    reminder_date = db.Column(db.DateTime, nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable=True)
    active = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(255), nullable=False)
    sent = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.id
