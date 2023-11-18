import React from 'react';
import Button from '@mui/material/Button';

const Buttons = ({ label, type }) => {
  const buttonStyle = {
    backgroundColor: '#1D0606', // Replace with your desired color
    color: 'white', // Text color
  };

  return (
    <Button 
    style={buttonStyle} 
    type={type}
    disabled={false} 
    variant="contained"
    onMouseEnter={(e) => (e.target.style.backgroundColor = '#b71c1c')}
    onMouseLeave={(e) => (e.target.style.backgroundColor = buttonStyle.backgroundColor)}>
      {label}
    </Button>
  );
};

export default Buttons;