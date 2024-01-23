import React, { useState } from "react";
import axios from "axios";

function Home() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:8000/accounts/register/", {
        username: username,
        password: password,
      })
      .then((response) => {
        console.log(response.data);
        // Gérer la réponse / redirection
      })
      .catch((error) => {
        console.error("There was an error!", error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Register</button>
    </form>
  );
}

export default Home;
