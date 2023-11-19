// import React from 'react';
// import { Link } from 'react-router-dom'; // If you're using React Router

// const Navbar = () => {
//   return (
//     <div className="sidebar">
//       <h2>Sidebar</h2>
//       <ul>
//         <li>
//           <Link to="/nprofile">Profile</Link>
//         </li>
//         <li>
//           <Link to="/skills">Skills and Ratings</Link>
//         </li>
//         <li>
//           <Link to="/dashboard">Paatient Dashboard</Link>
//         </li>
//       </ul>
//     </div>
//   );
// };

// export default Navbar;


import React, { useState } from 'react';

const Navbar = () => {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
    function openNav() {
        document.getElementById("mySidenav").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    }
    
    /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("main").style.marginLeft = "0";
        document.body.style.backgroundColor = "white";
    }

  return (
    <div className="container">
      <div id="mySidenav" className={`sidenav ${isSidebarOpen ? 'open' : ''}`}>
        <a href="javascript:void(0)" className="closebtn" onClick={closeNav}>&times;</a>
        <a href="/nprofile">Profile</a>
        <a href="/skills">Skills and Ratings</a>
        <a href="/dashboard">Patient Dashboard</a>
      </div>
      <span onClick={openNav}>open</span>
    </div>
  );

};

export default Navbar;