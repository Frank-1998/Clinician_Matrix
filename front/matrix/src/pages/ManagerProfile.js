import React from 'react';
import Buttons from '../components/Buttons';
import CustomTextFields from '../components/CustomTextFields';
import PasswordTextField from '../components/PasswordTextField';
import  "./ManagerProfile.css";
import AccountBoxRoundedIcon from '@mui/icons-material/AccountBoxRounded';
import LockRoundedIcon from '@mui/icons-material/LockRounded';
import axios from "axios";
import { useState } from "react";

const ManagerProfile = () => {
    /*
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs((values) => ({ ...values, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    let data;
    data = { // EDIT
      first_name: inputs["fname"],
      last_name: inputs["lname"],
      designation: inputs["designation"],
      y_nursing: inputs["ynursing"],
      hdata: inputs[],
      prev_exp: inputs[]
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
*/
  return (
    <div className="manager-profile-section">
      <h4>Login</h4>
      <form onSubmit={handleSubmit}>
        <div className="text_input">
          <CustomTextFields
            name="first_name"
            onChange={handleChange}
            label="fname"
            icon={<AccountBoxRoundedIcon />}
          ></CustomTextFields>
          {/* <Input defaultValue="Hello world" inputProps={ariaLabel} /> */}
        </div>
        <div className="text_input">
          <CustomTextField
            name="last_name"
            onChange={handleChange}
            label="lname"
            icon={<LockRoundedIcon />}
          ></CustomTextField>
        </div>
        <div>
          <Buttons label="SAVE" type="submit"></Buttons>
        </div>
      </form>
    </div>
  );
};

export default ManagerProfile;
