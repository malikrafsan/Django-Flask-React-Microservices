import { useEffect } from "react";
import axios from "axios";

export const Logout = () => {
  const logout = async () => {
    try {
      const { data } = await axios.post(
        "http://localhost:8000/auth/logout/",
        {
          refresh_token: localStorage.getItem("refresh_token"),
        },
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      console.log(data);
      
      localStorage.clear();
      axios.defaults.headers.common["Authorization"] = null;
      window.location.href = "/login";
    } catch (e) {
      console.log("logout not working", e);
    }
  };

  useEffect(() => {
    logout();
  }, []);
  return <div>Logout Page</div>;
};
