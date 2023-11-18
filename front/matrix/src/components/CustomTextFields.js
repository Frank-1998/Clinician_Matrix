import * as React from 'react';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';

const CustomTextFields = ({ label, icon, onChange, name }) => {
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
        style: { color: 'white' }, // Adjust color as needed
      }}
      label={label}
    />
  );
};

export default CustomTextFields;
