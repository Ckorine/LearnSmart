from backend.app.database.db import db


class Topic(db.Document):
    name = db.StringField(required=True, unique=True)
