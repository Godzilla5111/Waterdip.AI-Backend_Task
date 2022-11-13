from my_app import app, db
from my_app.models import Todo
from flask import request, render_template, jsonify
import json
import urllib.parse


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/v1/tasks/", methods=['GET', 'POST', 'DELETE'])
def todos():
    if request.method == 'POST':
        data = json.loads(request.data)
        # req = request.args.to_dict()
        if 'title' in data:           
            title = data['title']
            if 'is_completed' in data:
                is_completed = bool(data['is_completed'].lower())
                todo_instance =  Todo(title, is_completed)
                db.session.add(todo_instance)
            else:
                todo_instance =  Todo(title)
                db.session.add(todo_instance)
            db.session.commit()
            return {'id': todo_instance.id}, 201
        
        ### FOR BULK ADD ###
        elif 'tasks' in data:
            d = dict()
            d['tasks'] = []
            for instance in data['tasks']:
                if 'is_completed' in instance:
                    if type(instance['is_completed']) is bool:
                        is_completed = instance['is_completed']
                    else:
                        is_completed = bool(instance['is_completed'].lower())
                    todo_instance =  Todo(title=instance['title'], is_completed=is_completed)
                    db.session.add(todo_instance)
                else:
                    todo_instance =  Todo(title)
                    db.session.add(todo_instance)
                db.session.commit()
                d['tasks'].append({'id': todo_instance.id})
            return d, 201

    ### FOR BULK DELETE ###
    elif request.method == 'DELETE':
        data = json.loads(request.data)
        if 'tasks' in data:
            for instance in data['tasks']:
                try:
                    Todo.query.filter_by(id=instance['id']).delete()
                    db.session.commit()
                except:
                    continue
            return {'None':'None'}, 204
            
    elif request.method=='GET':
        return {'tasks':[x.as_dict() for x in Todo.query.all()]}, 200


@app.route("/v1/tasks/<int:id>/", methods=['GET', 'DELETE', 'PUT'])
def fetch_task(id):
    if request.method == 'GET':
        try:
            item = Todo.query.get(id)
            return item.as_dict(), 201
        except:
            return {'error':'There is no task at that id'}, 404
    elif request.method == 'DELETE':
        try:
            Todo.query.filter_by(id=id).delete()
            db.session.commit()
            return {'None':'None'}, 204
        except:
            return {'None':'None'}, 204
    elif request.method == 'PUT':
        data = json.loads(request.data)
        try:
            instance = Todo.query.get(id)
            if 'title' in data:
                instance.title = data['title']
            if 'is_completed' in data:
                is_completed = data['is_completed']
                if type(is_completed) is bool:
                    instance.is_completed = data['is_completed']
                else:
                    instance.is_completed = bool(data['is_completed'].lower())
            
            db.session.commit()
            return {'None':'None'}, 204
        except:
            return {'error': "There is no task at that id"}, 404






if __name__ == "__main__":
    app.run(debug=True)

