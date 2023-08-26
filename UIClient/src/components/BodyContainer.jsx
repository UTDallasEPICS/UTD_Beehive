// component with the tabs and the graph, connects to backend to get weight, temp, and humidity
import { useState, useEffect } from "react";

import Chart from "../components/Chart";

// import dummyData from "../data/dummyData.json";

import HivePageHeader from "./HivePageHeader";

import "../styles/bodyContainer.css";

const PI_IP_ADDRESS = "http://10.159.163.41"; // WARNING: IP ADDRESS MIGHT CHANGE 10.159.188.228
const PI_PORT_NUMBER = "5008";
const WEIGHT_DATA_ENDPOINT = "/databaseDataWeight";
const TEMPERATURE_DATA_ENDPOINT = "/databaseDataTemp";
const HUMIDITY_DATA_ENDPOINT = "/databaseDataHumidity";

function BodyContainer() {
  const [graphView, setGraphView] = useState("weight");
  const [graphData, setGraphData] = useState({});
  // const [weightData, setWeightData] = useState();
  // const [tempData, setTempData] = useState();

  useEffect(() => {
    let _weightData = null;
    let _tempData = null;
    let _humidityData = null;

    try {
      const fetchWeightData = async () => {
        // const res = await fetch("http://10.159.188.228:5008/databaseDataWeight");
        const res = await fetch(
          `${PI_IP_ADDRESS}:${PI_PORT_NUMBER}${WEIGHT_DATA_ENDPOINT}`
        );
        const data = await res.json();

        // console.log("Fetched Weight Graph Data: ", data.weightData);

        const weightData = data.weightData
          .filter((item) => item.testdata != null)
          .slice(-25);

        const formattedWeightData = weightData.map((item, index) => ({
          name: `Data ${index + 1}`,
          value: item.testdata,
        }));

        _weightData = formattedWeightData;
      };

      const fetchTempData = async () => {
        // const res = await fetch("http://10.159.188.228:5008/databaseDataTemp");
        const res = await fetch(
          `${PI_IP_ADDRESS}:${PI_PORT_NUMBER}${TEMPERATURE_DATA_ENDPOINT}`
        );
        const data = await res.json();

        // console.log("Fetched Temp Graph Data: ", data.tempData);

        const tempData = data.tempData.slice(-25);

        const formattedTempData = tempData.map((item, index) => ({
          name: `Data ${index + 1}`,
          value: item.testdata,
        }));

        _tempData = formattedTempData;
      };

      const fetchHumidData = async () => {
        // const res = await fetch("http://10.159.188.228:5008/databaseDataHumidity");
        const res = await fetch(
          `${PI_IP_ADDRESS}:${PI_PORT_NUMBER}${HUMIDITY_DATA_ENDPOINT}`
        );
        const data = await res.json();

        // console.log("Fetched Temp Graph Data: ", data.tempData);

        const humidityData = data.humidityData.slice(-25);

        const formattedHumidData = humidityData.map((item, index) => ({
          name: `Data ${index + 1}`,
          value: item.testdata,
        }));

        _humidityData = formattedHumidData;
      };

      const fetchAllData = async () => {
        await fetchWeightData();
        await fetchTempData();
        await fetchHumidData();

        const graphFormattedData = {
          weight: _weightData,
          temperature: _tempData,
          humidity: _humidityData,
        };

        console.log("Formatted Graph Data: ", graphFormattedData);

        setGraphData(graphFormattedData);
      };

      fetchAllData();
    } catch (err) {
      console.log("ERROR:", err.message);
    }
  }, []);

  const RenderGraphView = ({ currentGraphView }) => {
    switch (currentGraphView) {
      case "weight":
        return <Chart graphView={currentGraphView} data={graphData.weight} />;
      case "temp":
        return (
          <Chart graphView={currentGraphView} data={graphData.temperature} />
        );
      case "humidity":
        return <Chart graphView={currentGraphView} data={graphData.humidity} />;
      default:
        return <h1>Invalid Graph Type</h1>;
    }
  };

  // ternary oparator

  return (
    <div className="body-container">
      <HivePageHeader />

      <div className="tab">
        <button className="tabLinks" onClick={() => setGraphView("weight")}>
          Weight
        </button>
        <button className="tabLinks" onClick={() => setGraphView("temp")}>
          Temp
        </button>
        <button className="tabLinks" onClick={() => setGraphView("humidity")}>
          Humidity
        </button>
      </div>
      <div className="graph">
        {graphData ? (
          <RenderGraphView currentGraphView={graphView} />
        ) : (
          <p>Loading...</p>
        )}
      </div>
    </div>
  );
}

export default BodyContainer;
