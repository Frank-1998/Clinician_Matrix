import React from "react";
import Buttons from "../components/Buttons";
import CustomTextFields from "../components/CustomTextFields";
import PasswordTextField from "../components/PasswordTextField";
import "./LoginPage.css";
import AccountBoxRoundedIcon from "@mui/icons-material/AccountBoxRounded";
import LockRoundedIcon from "@mui/icons-material/LockRounded";
import axios from "axios";
import { useState } from "react";

const LoginPage = () => {
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs((values) => ({ ...values, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    let data;
    data = {
      username: inputs["username"],
      password: inputs["password"],
    };
    console.log(data);
    axios
      .post("http://127.0.0.1:8000/api/auth/login/", data)
      .then((res) => {
        console.log(res.data);
        const authToken = res.data.key;
        localStorage.setItem("authToken", authToken);
        if (authToken) {
          axios
            .get("http://127.0.0.1:8000/api/auth/user/", {
              headers: {
                Authorization: `Token ${authToken}`,
              },
            })
            .then((res) => {
              console.log(res.data);
              localStorage.setItem("user", res.data);
            })
            .catch((err) => {
              console.log(err);
            });
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="login-section">
      <h4>Login</h4>
      <form onSubmit={handleSubmit}>
        <div className="text_input">
          <CustomTextFields
            name="username"
            onChange={handleChange}
            label="Username"
            icon={<AccountBoxRoundedIcon />}
          ></CustomTextFields>
          {/* <Input defaultValue="Hello world" inputProps={ariaLabel} /> */}
        </div>
        <div className="text_input">
          <PasswordTextField
            name="password"
            onChange={handleChange}
            label="Password"
            icon={<LockRoundedIcon />}
          ></PasswordTextField>
        </div>
        <div>
          <Buttons label="Login" type="submit"></Buttons>
        </div>
      </form>
    </div>
  );
};

export default LoginPage;
