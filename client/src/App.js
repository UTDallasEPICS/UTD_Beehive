import './App.css'
import MainDash from './components/MainDash/MainDash';
import RightSide from './components/RigtSide/RightSide';
import Sidebar from './components/Sidebar';
import {HashRouter as Router, Route, Switch} from "react-router-dom";
import BeehiveView from "./components/BeehiveView";
import Dashboard from "./components/Dashboard";

function App() {
  return (
    <div className="App">
      <div className="AppGlass">
          <Router>
              <Sidebar/>
                <Switch>
                    <Route exact path="/" component={Dashboard}>
                    </Route>
                    <Route exact path="/beehive" component={BeehiveView}>
                    </Route>
              </Switch>
          </Router>
      </div>
    </div>
  );
}

export default App;
