from ..db import db
from .user import User


class UserForecastEvent(db.Model):
    __tablename__ = "user_events"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey(User.id))
    starts_at = db.Column(db.DateTime, nullable=False)
    ends_at = db.Column(db.DateTime)
    timetable = db.column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<UserForecastEvent { self.email }>"
