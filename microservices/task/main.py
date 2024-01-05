from flask import Flask, request 
import sqlite3 
from models import Task, Status
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

    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM tasks where username = ?', (username,))
  
    data = cursor.fetchall()
    blogs = [Task.deserialize(datum) for datum in data]

    return {
      'status': 'success',
      'message': 'task retrieved successfully',
      'data': blogs
    }
   
  elif request.method == 'POST':
    username = request.json['username']
    title = request.json['title']
    description = request.json['description']
    status = Status.TODO.to_str()

    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor() 
    cursor.execute("INSERT INTO tasks (username, title, description, status) VALUES (?,?,?,?)", (username, title, description, status))
    connect.commit()

    blog_id = cursor.lastrowid

    task = Task(blog_id, username, title, description, status)

    return {
      'status': 'success',
      'message': 'blog created successfully',
      'data': task.to_json()
    }

@app.route("/task/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def task_detail(id):
  if request.method == 'GET':
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM tasks where id = ?', (id,))
  
    data = cursor.fetchone()
    task = Task.deserialize(data)

    return {
      'status': 'success',
      'message': 'task retrieved successfully',
      'data': task.to_json()
    }
   
  elif request.method == 'PUT':
    title = request.json['title']
    description = request.json['description']
    status = request.json['status']

    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor() 
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?", (title, description, status, id))
    connect.commit()

    task = Task(id, title, description, status)

    return {
      'status': 'success',
      'message': 'task updated successfully',
      'data': task.to_json()
    }

  elif request.method == 'DELETE':
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor() 
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    connect.commit()

    return {
      'status': 'success',
      'message': 'task deleted successfully',
    }

if __name__ == '__main__': 
  app.wsgi_app = APIKeyMiddleware(app.wsgi_app)
  app.run(debug=True)
 
