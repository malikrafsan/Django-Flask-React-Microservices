from flask import Flask, request 
import sqlite3 
from models import Blog

app = Flask(__name__) 

DB_PATH = "db/db.sqlite3"
SCHEMA_PATH = "db/schema.sql"

# remove db file
import os
if os.path.exists(DB_PATH):
  os.remove(DB_PATH)

connect = sqlite3.connect(DB_PATH)
with open(SCHEMA_PATH, 'r') as f: 
  connect.executescript(f.read())
	
@app.route("/blog", methods=['GET', 'POST'])
def blog():
  if request.method == 'GET':
    username = request.args.get('username')

    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM blogs where username = ?', (username,))
  
    data = cursor.fetchall()
    blogs = [Blog.deserialize(datum) for datum in data]

    return {
      'status': 'success',
      'message': 'blog retrieved successfully',
      'data': blogs
    }
   
  elif request.method == 'POST':
    username = request.form['username']
    title = request.form['title']
    content = request.form['content']

    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor() 
    cursor.execute("INSERT INTO blogs (username, title, content) VALUES (?,?,?)", (username, title, content))
    connect.commit()

    blog_id = cursor.lastrowid

    return {
      'status': 'success',
      'message': 'blog created successfully',
      'data': {
        'id': blog_id,
        'username': username,
        'title': title,
        'content': content
      }
    }

if __name__ == '__main__': 
	app.run(debug=False) 
