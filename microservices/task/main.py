from flask import Flask, request
import sqlite3
from models import Task, Status
from repositories import TaskRepo
from middlewares import APIKeyMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

DB_PATH = "db/db.sqlite3"
SCHEMA_PATH = "db/schema.sql"


if os.path.exists(DB_PATH):
    try:
        os.remove(DB_PATH)
    except:
        print("Error while deleting file ", DB_PATH)

connect = sqlite3.connect(DB_PATH)
with open(SCHEMA_PATH, 'r') as f:
    connect.executescript(f.read())


@app.route("/task", methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        username = request.args.get('username')

        task_repo = TaskRepo(DB_PATH)
        tasks = task_repo.fetch_by_username(username)

        return {
            'status': 'success',
            'message': 'task retrieved successfully',
            'data': tasks
        }

    elif request.method == 'POST':
        username = request.json['username']
        title = request.json['title']
        description = request.json['description']
        status = Status.TODO.to_str()

        task = Task(None, title, description, status, username)

        task_repo = TaskRepo(DB_PATH)

        task = task_repo.create(task)

        return {
            'status': 'success',
            'message': 'task created successfully',
            'data': task.to_json()
        }


@app.route("/task/<int:id>", methods=['GET', 'PATCH', 'DELETE'])
def task_detail(id):
    if request.method == 'GET':
        task_repo = TaskRepo(DB_PATH)
        task = task_repo.fetch_by_id(id)

        username = request.args.get('username')

        if task.username != username:
            return {
                'status': 'error',
                'message': 'username is invalid',
            }, 401

        return {
            'status': 'success',
            'message': 'task retrieved successfully',
            'data': task.to_json()
        }

    elif request.method == 'PATCH':
        username = request.args.get('username')

        task_repo = TaskRepo(DB_PATH)
        task = task_repo.fetch_by_id(id)

        if task.username != username:
            return {
                'status': 'error',
                'message': 'username is invalid',
            }, 401

        task.status = request.json['status']
        task = task_repo.update(task)

        return {
            'status': 'success',
            'message': 'task updated successfully',
            'data': task.to_json()
        }

    elif request.method == 'DELETE':
        username = request.args.get('username')

        task_repo = TaskRepo(DB_PATH)
        task = task_repo.fetch_by_id(id)

        if task.username != username:
            return {
                'status': 'error',
                'message': 'username is invalid',
            }, 401

        task_repo.delete(id)

        return {
            'status': 'success',
            'message': 'task deleted successfully',
        }


if __name__ == '__main__':
    app.wsgi_app = APIKeyMiddleware(app.wsgi_app)
    app.run(debug=True, port=5002)
