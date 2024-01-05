import sqlite3
from models import Blog

class BlogRepo:
  def __init__(self, db_path):
    self.db_path = db_path
  
  def fetch_by_username(self, username):
    connect = sqlite3.connect(self.db_path)
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM blogs where username = ?', (username,))
  
    data = cursor.fetchall()
    blogs = [Blog.deserialize(datum) for datum in data]

    return blogs
  
  def create_blog(self, blog: Blog):
    connect = sqlite3.connect(self.db_path)
    cursor = connect.cursor() 
    cursor.execute("INSERT INTO blogs (username, title, content) VALUES (?,?,?)", (blog.username, blog.title, blog.content))
    connect.commit()

    blog_id = cursor.lastrowid
    blog.id = blog_id

    return blog
