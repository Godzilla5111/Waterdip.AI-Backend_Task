from ..my_app import app,db
from my_app.models import Todo

todo1 = Todo("Sample Title", True)

with app.app_context():
    db.session.add(todo1)
    db.session.commit()