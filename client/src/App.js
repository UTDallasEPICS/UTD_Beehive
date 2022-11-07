import './App.css'
import MainDash from './components/MainDash/MainDash';
import RightSide from './components/RigtSide/RightSide';
import Sidebar from './components/Sidebar';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import BeehiveView from "./components/BeehiveView";

function App() {
  return (
    <div className="App">
      <div className="AppGlass">
          <Router>
              <Sidebar/>
                <Switch>
                    <Route exact path="/">
                        <MainDash/>
                        <RightSide/>
                    </Route>
                    <Route exact path="/beehive">
                        <BeehiveView/>
                    </Route>
              </Switch>
          </Router>
      </div>
    </div>
  );
}

export default App;
