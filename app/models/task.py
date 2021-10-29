from flask import current_app
from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        complete = False
        if self.completed_at:
            complete = True

        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": complete
        }