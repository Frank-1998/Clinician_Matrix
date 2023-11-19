import logo from './images/logoText.png';
import Buttons from './components/Buttons';
import './App.css';
import PersonAddAltRoundedIcon from '@mui/icons-material/PersonAddAltRounded';
import AccountCircleRoundedIcon from '@mui/icons-material/AccountCircleRounded';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <div className="landing-page-section">
      <img src={logo} className="App-logo" alt="logo" />
      <h2>Welcome!</h2>
      <div className="flex-container">
        <div className="flex-container">
          <h4>Getting Started?</h4>
          <div className="button">
            <Buttons label="Signup As Nurse" icon={<PersonAddAltRoundedIcon />} />
          </div>
          <div className="button">
            <Buttons label="Signup As Manager" icon={<PersonAddAltRoundedIcon />} />
          </div>
        </div>
        <div className="flex-container">
          <h4>Returning User?</h4>
          <div>
            <Buttons label="Login As Nurse" icon={<AccountCircleRoundedIcon />} />
          </div>
          <div>
            <Buttons label="Login As Manager" icon={<AccountCircleRoundedIcon />} />
          </div>
        </div>
      </div>
    </div>
      <a
          className="App-link"
          //href="https://reactjs.org"
          href="/login"
          target="_blank"
          rel="noopener noreferrer"
        >
          Login
        </a>
        <a
          className="App-link"
          //href="https://reactjs.org"
          href="/signup"
          target="_blank"
          rel="noopener noreferrer"
        >
          Signup
        </a>
        <a
          className="App-link"
          //href="https://reactjs.org"
          href="/dashboard"
          target="_blank"
          rel="noopener noreferrer"
        >
          Patient Dashboard
        </a>
        <a
          className="App-link"
          href="/skills"
          target="_blank"
          rel="noopener noreferrer"
        >
          Skills
        </a>
      </header>
    </div>
  );
}

export default App;
