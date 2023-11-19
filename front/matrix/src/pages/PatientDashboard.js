import React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import "./PatientDashboardPage.css";
import { useState, useEffect } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

// let data = ['Skill Name 1', 'Skill Name 2', 'Skill Name 3', 'Skill Name 4', "Skill Name 5"];
function createData(patientName, nurseAvailable) {
  return { patientName, nurseAvailable };
}

// const rows = [
//   createData("Patient 1", ["Skill 1 ", "skills2"], "Nurse 1"),
//   createData("Patient 2", "Skill 2", "Nurse 2"),
//   createData("Patient 3", "Skill 3", "Nurse 3"),
//   createData("Patient 4", "Skill 4", "Nurse 4"),
//   createData("Patient 5", "Skill 5", "Nurse 5"),
// ];

function extractData(pt, skills, assignment) {
  const assign = assignment.assignment;
  const resultArray = [];
  for (const nurseKey in assign) {
    if (assign.hasOwnProperty(nurseKey)) {
      const patientArray = assign[nurseKey];
      patientArray.forEach((patient) => {
        resultArray.push([patient, nurseKey]);
      });
    }
  }
  console.log(resultArray);
  return resultArray;
}

function PatientDashboardPage() {
  const [assign, setAssign] = useState({});
  const [pt, setPt] = useState({});
  const [skills, setSkill] = useState({});
  const getAssignment = () => {
    axios
      .get("http://127.0.0.1:8000/api/assign/")
      .then((res) => {
        // console.log(res.data);
        setAssign(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const getPt = () => {
    axios
      .get("http://127.0.0.1:8000/api/patients/")
      .then((res) => {
        setPt(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  const getSkill = () => {
    axios
      .get("http://127.0.0.1:8000/api/skills/")
      .then((res) => {
        setSkill(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  useEffect(() => {
    getAssignment();
    getPt();
    getSkill();
  }, []);
  const result = extractData(pt, skills, assign);
  console.log(result);
  const rows = [];
  for (let i = 0; i < result.length; i++) {
    const data = createData(result[i][0], result[i][1]);
    rows.push(data);
  }

  return (
    <div className="patient-dashboard-section">
      <Navbar></Navbar>
      <h2>Patient Assignment Dashboard</h2>

      <div className="patient-dashboard-section" class="flex-container">
        <div className="text_input">
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell align="center">Patient Name</TableCell>
                  <TableCell align="center">Nurse Available</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {rows.map((data) => (
                  <TableRow
                    key={data}
                    sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                  >
                    <TableCell component="th" scope="row" align="center">
                      {data.patientName}
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
