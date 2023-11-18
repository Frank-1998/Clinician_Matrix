// PasswordInput.js

import React from 'react';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';

const PasswordTextField = ({ label, icon, onChange, name }) => {
  const iconStyle = {
    color: 'white', // Text color
  };
  const textStyle = {
    backgroundColor: '#1D0606', // Background color
    color: 'white', // Text color
  };

  return (
    <TextField
      name={name}
      onChange={onChange}
      style={textStyle}
      variant="filled"
      fullWidth
      type="password"  // Set type to 'password'
      InputProps={{
        inputProps: {
            style: { color: 'white' }, // Text color when typing
        },
        startAdornment: (
          <InputAdornment position="start" style={iconStyle}>
            {icon}
          </InputAdornment>
        ),
      }}
      InputLabelProps={{
        style: { color: 'white' }, // Label color
      }}
      label={label}
    />
  );
};

export default PasswordTextField;