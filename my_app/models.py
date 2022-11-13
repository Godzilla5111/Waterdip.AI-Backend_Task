from my_app import db

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    is_completed = db.Column(db.Boolean, nullable=False)

    def __init__(self, title, is_completed=False):
        self.title = title
        self.is_completed = is_completed

    def __repr__(self):
        return f"The title of the task is {self.title} and the completion status of the task is {self.is_completed}."
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
