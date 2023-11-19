import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import CustomTextField from '../components/CustomTextFields';
import Buttons from '../components/Buttons';
import './NurseProfile.css';
import Navbar from '../components/Navbar';

function NurseProfile() {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    designation: '',
    years_of_nursing: '',
    hire_date: null, // Set hire_date to null initially
    previous_experience: '',
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Form submitted!', formData);
    // Add any additional logic for form submission
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleDateChange = (date) => {
    setFormData((prevData) => ({
      ...prevData,
      hire_date: date,
    }));
  };

  return (
    <div className="nurse-profile-section">
      <Navbar></Navbar>
      <h4>Nurse Profile</h4>
      <form onSubmit={handleSubmit}>
        <div className="text_input">
          <CustomTextField
            name="first_name"
            onChange={handleChange}
            label="First Name"
          />
        </div>
        <div className="text_input">
          <CustomTextField
            name="last_name"
            onChange={handleChange}
            label="Last Name"
          />
        </div>
        <div className="text_input">
          <CustomTextField
            name="designation"
            onChange={handleChange}
            label="Designation"
          />
        </div>
        <div className="text_input">
          <CustomTextField
            name="years_of_nursing"
            onChange={handleChange}
            label="Years of Nursing"
          />
        </div>
        <div className="text_input">
          {/* Use the DatePicker component for the hire_date */}
          <DatePicker
            selected={formData.hire_date}
            onChange={handleDateChange}
            dateFormat="MM/dd/yyyy"
            placeholderText="Hire Date"
          />
        </div>
        <div className="text_input">
          <CustomTextField
            name="previous_experience"
            onChange={handleChange}
            label="Previous Experience"
            multiline
          />
        </div>
        <div>
          <Buttons label="SAVE" type="submit" />
        </div>
      </form>
    </div>
  );
}

export default NurseProfile;