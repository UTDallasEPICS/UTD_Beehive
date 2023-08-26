import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import SideBar from "./components/SideBar";
import BodyContainer from "./components/BodyContainer";
import BodyTxtContainer from "./components/BodyTxtContainer";
import AvgContainer from "./components/AvgContainer";

import "./styles/app.css";

function App() {
  return (
    <div className="App">
      <Header />
      <SideBar />
      {/* <BodyContainer /> */}

      <Router>
        <Routes>
          <Route
            exact
            path="/"
            element={
              <BodyTxtContainer
                title="Dashboard"
                text="Welcome to the dashboard"
              />
            }
          />
          <Route
            path="/beehives"
            element={
              <div className="hivePage-container">
                <BodyContainer />
                <div className="avg-containers">
                  <AvgContainer heading="Weight" number="26" color="#e5ba73" />
                  <AvgContainer heading="Temp" number="73" color="#c58940" />
                  <AvgContainer
                    heading="Humidity"
                    number="49"
                    color="#ffd56f"
                  />
                </div>
              </div>
            }
          />
          <Route
            path="/insights"
            element={
              <BodyTxtContainer
                title="Insights"
                text="Welcome to the insights page"
              />
            }
          />
          <Route
            path="/archived"
            element={
              <BodyTxtContainer
                title="Archived"
                text="Welcome to the archived page"
              />
            }
          />
          <Route
            path="/settings"
            element={
              <BodyTxtContainer
                title="Settings"
                text="Welcome to the settings page"
              />
            }
          />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

// how to place child elements equall spaced out on a webpage in a row

// read about flex box in CSS
// get done with React tutorials
// get a overview of HTML, CSS & JavaScript
