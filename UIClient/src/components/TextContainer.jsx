import "../styles/textContainer.css";

function TextContainer() {
  return (
    <li className="container">
      <p className="title">Title</p>
      <p className="body">Text goes here</p>

      <div className="tab">
        <button className="tabLinks" onClick={() => setGraphView(1)}>
          Weight
        </button>
        <button className="tabLinks" onClick={() => setGraphView(2)}>
          Temp
        </button>
        <button className="tabLinks" onClick={() => setGraphView(3)}>
          Humidity
        </button>
      </div>

      {renderGraphView(graphView)}
    </li>
  );
}

export default TextContainer;
