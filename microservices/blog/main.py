from flask import Flask, request 
import sqlite3 
from models import Blog
from middlewares import APIKeyMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__) 

DB_PATH = "db/db.sqlite3"
SCHEMA_PATH = "db/schema.sql"

# remove db file

if os.path.exists(DB_PATH):
  try:
    os.remove(DB_PATH)
  except:
    print("Error while deleting file ", DB_PATH)

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
    username = request.json['username']
    title = request.json['title']
    content = request.json['content']

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
  app.wsgi_app = APIKeyMiddleware(app.wsgi_app)
  app.run(debug=True)
 
