// import { Link } from "react-router-dom";

import "../styles/sidebar.css";

function SideBar() {
  return (
    <>
      <div className="sidebar-container">
        <a href="/" className="sidebar">
          Dashboard
        </a>
        {/* <Link to={"beehives"}>Dashboard</Link> */}
        <a href="/beehives" className="sidebar">
          BeeHives
        </a>
        <a href="/insights" className="sidebar">
          Insights
        </a>
        <a href="/archived" className="sidebar">
          Archived
        </a>
        <a href="/settings" className="sidebar">
          Settings
        </a>
      </div>
    </>
  );
}

export default SideBar;
