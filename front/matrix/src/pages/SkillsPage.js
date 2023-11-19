import React from 'react';
import Dropdown from '../components/Dropdown';
import Buttons from '../components/Buttons';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import  "./SkillsPage.css";
import Navbar from '../components/Navbar';

let items = ['Skill Name 1', 'Skill Name 2', 'Skill Name 3', 'Skill Name 4', "Skill Name 5"];

function SkillsPage() {
  return (
    <div className="skills-section">
      <Navbar></Navbar>
      <h2>Skills and Ratings</h2>

      <div className="skills-section" class='flex-container'>
        
        <div className="text_input">
          <h3>Level 1 Skills</h3>
            <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell align="center">Skill Name</TableCell>
                <TableCell align="center">Rating</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {items.map((item) => (
                <TableRow
                  key={item}
                  sx={{ '&:last-child td, &:last-child th': { border: 0} }}>
                  <TableCell component="th" scope="row" align="center">
                    {item}
                  </TableCell>
                  <TableCell align="center">
                    <Dropdown className="dropdown"></Dropdown>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
            </Table>
            </TableContainer>
        </div>

        <div className="text_input">
          <h3>Level 2 Skills</h3>
            <TableContainer component={Paper}>
            <Table sx={{minWidth: 650}} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell align="center">Skill Name</TableCell>
                <TableCell align="center">Rating</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {items.map((item) => (
                <TableRow
                  key={item}
                  sx={{ '&:last-child td, &:last-child th': { border: 0} }}>
                  <TableCell component="th" scope="row" align="center">
                    {item}
                  </TableCell>
                  <TableCell align="center">
                    <Dropdown className="dropdown"></Dropdown>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
            </Table>
            </TableContainer>
        </div>
        
        <div className="text_input">
          <h3>Level 3 Skills</h3>
            <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell align="center">Skill Name</TableCell>
                <TableCell align="center">Rating</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {items.map((item) => (
                <TableRow
                  key={item}
                  sx={{ '&:last-child td, &:last-child th': { border: 0} }}>
                  <TableCell component="th" scope="row" align="center">
                    {item}
                  </TableCell>
                  <TableCell align="center">
                    <Dropdown className="dropdown"></Dropdown>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
            </Table>
            </TableContainer>
        </div>

        <div>
          <Buttons label="Save" type="submit"></Buttons>
        </div>
  
      </div>
      
    </div>

  );
}

export default SkillsPage;
