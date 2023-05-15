// displays inputted title and text- used for showing dashboard, insights, archived and settings pages in website
import React from "react";

import "../styles/bodyTxtContainer.css";

function BodyTxtContainer(props) {
  return (
    <div className="container">
      <h1 className="title">{props.title}</h1>
      <p className="body">{props.text}</p>
    </div>
  );
}

export default BodyTxtContainer;
