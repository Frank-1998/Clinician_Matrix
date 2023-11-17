import React from 'react';
import Buttons from '../components/Buttons';
import CustomTextFields from '../components/CustomTextFields';
import PasswordTextField from '../components/PasswordTextField';
import  "./LoginPage.css";
import AccountBoxRoundedIcon from '@mui/icons-material/AccountBoxRounded';
import LockRoundedIcon from '@mui/icons-material/LockRounded';

function LoginPage() {
    return (
        <div className="login-section">
        <h4>Login</h4>
        <form>
          <div className="text_input">
            <CustomTextFields label="Username" icon={<AccountBoxRoundedIcon/>}></CustomTextFields>
            {/* <Input defaultValue="Hello world" inputProps={ariaLabel} /> */}
          </div>
          <div className="text_input">
            <PasswordTextField label="Password" icon={<LockRoundedIcon/>}></PasswordTextField>
          </div>
          <div>
            <Buttons label="Login"></Buttons>
          </div>
        </form>
      </div>
    )
}

export default LoginPage

