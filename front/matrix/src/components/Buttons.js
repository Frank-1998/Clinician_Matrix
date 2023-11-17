import React from 'react';
import Button from '@mui/material/Button';

const Buttons = ({ label }) => {
  const buttonStyle = {
    backgroundColor: '#1D0606', // Replace with your desired color
    color: 'white', // Text color
  };

  return (
    <Button style={buttonStyle} disabled={false} variant="contained">
      {label}
    </Button>
  );
};

export default Buttons;