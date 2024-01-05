import sqlite3
from models import Task


class TaskRepo:
  def __init__(self, db_path):
    self.db_path = db_path

  def fetch_by_username(self, username):
    connect = sqlite3.connect(self.db_path)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM tasks where username = ?', (username,))

    data = cursor.fetchall()
    tasks = [Task.deserialize(datum) for datum in data]
    json_tasks = [task.to_json() for task in tasks]

    return json_tasks
  
  def fetch_by_id(self, task_id):
    connect = sqlite3.connect(self.db_path)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM tasks where id = ?', (task_id,))

    data = cursor.fetchone()
    task = Task.deserialize(data)

    return task

  def create(self, task: Task):
    connect = sqlite3.connect(self.db_path)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO tasks (username, title, description, status) VALUES (?,?,?,?)",
                   (task.username, task.title, task.description, task.status))
    connect.commit()

    task_id = cursor.lastrowid
    task.id = task_id

    return task
  
  def update(self, task: Task):
    connect = sqlite3.connect(self.db_path)
    cursor = connect.cursor()
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?",
                   (task.title, task.description, task.status, task.id))
    connect.commit()

    return task
  
  def delete(self, task_id: int):
    connect = sqlite3.connect(self.db_path)
    cursor = connect.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connect.commit()
  


