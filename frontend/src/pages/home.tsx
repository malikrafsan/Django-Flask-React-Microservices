import { useEffect, useState } from "react";
import axios from "axios";
import { AddBlogModal } from "../components/add-blog-modal";
import { AddTaskModal } from "../components/add-task-modal";
import { Blog, Task } from "../types";

export const Home = () => {
  const [message, setMessage] = useState("");
  const [showAddBlogModal, setShowAddBlogModal] = useState(false);
  const [showAddTaskModal, setShowAddTaskModal] = useState(false);
  const [blogs, setBlogs] = useState<Blog[]>([]);
  const [tasks, setTasks] = useState<Task[]>([]);

  const getMessage = async () => {
    try {
      const { data } = await axios.get("http://localhost:8000/home/", {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      });
      setMessage(data.message);
    } catch (e) {
      console.log("not auth");
    }
  };

  const getBlogs = async () => {
    try {
      const { data } = await axios.get("http://localhost:8000/blog/", {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      });
      console.log(data);
      setBlogs(data.data);
    } catch (e) {
      console.log("error", e);
    }
  };

  const getTasks = async () => {
    try {
      const { data } = await axios.get("http://localhost:8000/task/", {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      });
      console.log(data);

      setTasks(data.data);
    } catch (e) {
      console.log("error", e);
    }
  };

  const editTask = async (id: number, status: string) => {
    try {
      const { data } = await axios.patch(
        `http://localhost:8000/task/${id}/`,
        {
          status,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        }
      );
      console.log(data);
      getTasks();
    } catch (e) {
      console.log("error", e);
    }
  }

  const deleteTask = async (id: number) => {
    try {
      const { data } = await axios.delete(
        `http://localhost:8000/task/${id}/`,
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        }
      );
      console.log(data);
      getTasks();
    } catch (e) {
      console.log("error", e);
    }
  }

  useEffect(() => {
    if (!localStorage.getItem("access_token")) {
      window.location.href = "/login";
      return;
    }

    getMessage();
    getTasks();
    getBlogs();
  }, []);

  return (
    <div className="form-signin my-5 text-center">
      <h2>Hi {message}</h2>
      <div className="p-3">
        <div className="d-flex justify-content-between">
          <h2 className="text-start">Blog</h2>

          <button
            className="btn btn-primary"
            onClick={() => setShowAddBlogModal(true)}
          >
            Add Blog
          </button>
        </div>
        <div>
          {blogs.map((blog) => (
            <div className="card mt-3" key={blog.id}>
              <div className="card-body">
                <h5 className="card-title">{blog.title}</h5>
                <p className="card-text">{blog.content}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
      <hr></hr>
      <div className="p-3">
        <div className="d-flex justify-content-between">
          <h2 className="text-start">Task</h2>

          <button
            className="btn btn-primary"
            onClick={() => setShowAddTaskModal(true)}
          >
            Add Task
          </button>
        </div>
        <div>
          {tasks.map((task) => (
            <div className="card mt-3" key={task.id}>
              <div className="card-body">
                <h5 className="card-title">{task.title} ({task.status})</h5>
                <p className="card-text">{task.description}</p>
              </div>
              <div className="d-flex justify-content-between">
                <button className="btn btn-primary"
                  onClick={() => editTask(task.id, "doing")}
                >Doing</button>
                <button className="btn btn-success"
                  onClick={() => editTask(task.id, "done")}
                >Done</button>
                <button className="btn btn-danger"
                  onClick={() => deleteTask(task.id)}
                >Delete</button>
              </div>
            </div>
          ))}
        </div>
      </div>

      <AddBlogModal
        show={showAddBlogModal}
        handleClose={() => {
          setShowAddBlogModal(false);
          getBlogs();
        }}
      />
      <AddTaskModal
        show={showAddTaskModal}
        handleClose={() => {
          setShowAddTaskModal(false);
          getTasks();
        }}
      />
    </div>
  );
};
