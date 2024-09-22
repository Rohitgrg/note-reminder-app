from datetime import datetime, timezone

from project.db import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable=True)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.id
