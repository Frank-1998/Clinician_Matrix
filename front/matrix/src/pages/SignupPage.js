import React from 'react';
import Buttons from '../components/Buttons';
import CustomTextFields from '../components/CustomTextFields';
import PasswordTextField from '../components/PasswordTextField';
import  "./SignupPage.css";
import AccountBoxRoundedIcon from '@mui/icons-material/AccountBoxRounded';
import LockRoundedIcon from '@mui/icons-material/LockRounded';
import EmailRoundedIcon from '@mui/icons-material/EmailRounded';

function SignupPage() {
    return (
        <div className="signup-section">
        <h4>Signup</h4>
        <form>
          <div className="text_input">
            <CustomTextFields label="Create Username" icon={<AccountBoxRoundedIcon/>}></CustomTextFields>
            {/* <Input defaultValue="Hello world" inputProps={ariaLabel} /> */}
          </div>
          <div className="text_input">
            <CustomTextFields label="Email" icon={<EmailRoundedIcon/>}></CustomTextFields>
          </div>
          <div className="text_input">
            <PasswordTextField label="Create Password" icon={<LockRoundedIcon/>}></PasswordTextField>
          </div>
          <div className="text_input">
            <PasswordTextField label="Confirm Password" icon={<LockRoundedIcon/>}></PasswordTextField>
          </div>
          <div>
            <Buttons label="Create Account" pageLink={"/nprofile"}></Buttons>
          </div>
        </form>
      </div>
    )
}

export default SignupPage

