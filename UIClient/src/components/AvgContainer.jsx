// show inputted text, data value and color- can be used to display quick stats like avg eight etc
import React from "react";

import "../styles/avgContainer.css";

function AvgContainer(props) {
  return (
    <div className="avg-container" style={{ backgroundColor: props.color }}>
      <h1 className="heading">{props.heading}</h1>
      <p className="number">{props.number}</p>
    </div>
  );
}

export default AvgContainer;
