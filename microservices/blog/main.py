from flask import Flask, request 
import sqlite3 
from models import Blog
from repositories import BlogRepo
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
	
@app.route("/blog", methods=['GET', 'POST'])
def blog():
  if request.method == 'GET':
    username = request.args.get('username')

    blog_repo = BlogRepo(DB_PATH)
    blogs = blog_repo.fetch_by_username(username)

    return {
      'status': 'success',
      'message': 'blog retrieved successfully',
      'data': blogs
    }
   
  elif request.method == 'POST':
    username = request.json['username']
    title = request.json['title']
    content = request.json['content']

    blog = Blog(None, username, title, content)

    blog_repo = BlogRepo(DB_PATH)
    blog = blog_repo.create(blog)

    return {
      'status': 'success',
      'message': 'blog created successfully',
      'data': blog.to_json()
    }

if __name__ == '__main__': 
  app.wsgi_app = APIKeyMiddleware(app.wsgi_app)
  app.run(debug=True)
 
