// Import the react JS packages
import axios from "axios";
import { useState, FormEvent } from "react";
// Define the Register function.

export const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const onSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const user = {
      username,
      password,
    };

    try {
          const { data } = await axios.post("http://localhost:8000/auth/register/", user, {
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true,
    });
    console.log(data);

    window.location.href = "/login";
    } catch (e) {
      alert("error" + JSON.stringify(e));
      console.log(e);
    }
  };

  return (
    <div className="Auth-form-container">
      <form className="Auth-form" onSubmit={onSubmit}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign Up</h3>
          <div className="form-group mt-3">
            <label>Username</label>
            <input
              className="form-control mt-1"
              placeholder="Enter Username"
              name="username"
              type="text"
              value={username}
              required
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="form-group mt-3">
            <label>Password</label>
            <input
              name="password"
              type="password"
              className="form-control mt-1"
              placeholder="Enter password"
              value={password}
              required
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};
