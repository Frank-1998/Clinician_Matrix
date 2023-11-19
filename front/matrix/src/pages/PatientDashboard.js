import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import  "./PatientDashboardPage.css";
import Navbar from '../components/Navbar';



// let data = ['Skill Name 1', 'Skill Name 2', 'Skill Name 3', 'Skill Name 4', "Skill Name 5"];
function createData(patientName, skillsRequired, nurseAvailable) {
    return { patientName, skillsRequired, nurseAvailable};
  }
  
const rows = [
    createData('Patient 1', "Skill 1", "Nurse 1"),
    createData('Patient 2', "Skill 2", "Nurse 2"),
    createData('Patient 3', "Skill 3", "Nurse 3"),
    createData('Patient 4', "Skill 4", "Nurse 4"),
    createData('Patient 5', "Skill 5", "Nurse 5"),
];

function PatientDashboardPage() {
  return (
    <div className="patient-dashboard-section">
      <Navbar></Navbar>
      <h2>Patient Assignment Dashboard</h2>

      <div className="patient-dashboard-section" class='flex-container'>
        <div className="text_input">
            <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell align="center">Patient Name</TableCell>
                <TableCell align="center">Skills Required</TableCell>
                <TableCell align="center">Nurse Available</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map((data) => (
                <TableRow
                  key={data}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                  <TableCell component="th" scope="row" align="center">
                    {data.patientName}
                  </TableCell>
                  <TableCell component="th" scope="row" align="center">
                    {data.skillsRequired}
                  </TableCell>
                  <TableCell component="th" scope="row" align="center">
                    {data.nurseAvailable}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
            </Table>
            </TableContainer>
        </div>

     </div>

    </div>



  );
}

export default PatientDashboardPage;