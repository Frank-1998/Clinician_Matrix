import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
          HELLO
        </p>
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
        <a
          className="App-link"
          href="/mprofile"
          target="_blank"
          rel="noopener noreferrer"
        >
          Manager Profile
        </a>
        <a
          className="App-link"
          href="/nprofile"
          target="_blank"
          rel="noopener noreferrer"
        >
          Nurse Profile
        </a>
      </header>
    </div>
  );
}

export default App;
