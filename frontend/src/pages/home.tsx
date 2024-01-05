import { useEffect, useState } from "react";
import axios from "axios";
import { AddBlogModal } from "../components/add-blog-modal";
import { Blog } from "../types";

export const Home = () => {
  const [message, setMessage] = useState("");
  const [showAddBlogModal, setShowAddBlogModal] = useState(false);
  const [blogs, setBlogs] = useState<Blog[]>([]); 

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
  }

  useEffect(() => {
    if (!localStorage.getItem("access_token")) {
      window.location.href = "/login";
      return;
    }
    
    getMessage();
    getBlogs();
  }, []);

  return (
    <div className="form-signin mt-5 text-center">
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
          {
            blogs.map((blog) => (
              <div className="card mt-3" key={blog.id}>
                <div className="card-body">
                  <h5 className="card-title">{blog.title}</h5>
                  <p className="card-text">{blog.content}</p>
                </div>
              </div>
            ))
          }
        </div>
      </div>

      <AddBlogModal
        show={showAddBlogModal}
        handleClose={() => {
          setShowAddBlogModal(false);
        }}
      />
    </div>
  );
};
