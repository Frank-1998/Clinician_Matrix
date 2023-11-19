import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

const Dropdown= ({onChange}) => {
  const [rating, setRating] = React.useState('');

  const handleChange = (event) => {
    setRating(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 100 }}> 
      <FormControl style={{ width:90 }}>
        <InputLabel id="demo-simple-select-label">Rating</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={rating}
          label="Rating"
          onChange={handleChange}>
          <MenuItem value={10}>1</MenuItem>
          <MenuItem value={20}>2</MenuItem>
          <MenuItem value={30}>3</MenuItem>
          <MenuItem value={40}>4</MenuItem>
          <MenuItem value={50}>5</MenuItem>
        </Select>
      </FormControl>
    </Box>
  );
}

export default Dropdown;
