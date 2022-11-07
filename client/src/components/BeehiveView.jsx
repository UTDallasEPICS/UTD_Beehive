import React, {useState} from "react";
import Chart from "react-apexcharts";

const BeehiveView = () => {
    const [state, setState] = useState({
        options: {
            colors: ["#E91E63", "#FF9800"],
            chart: {
                id: "basic-bar",
            },
            xaxis: {
                categories: [1, 2, 3, 4, 5, 6, 7, 8, 9],
            },
        },
        series: [
            {
                name: "var x",
                data: [30, 40, 45, 50, 49, 60, 70, 91],
            },
            {
                name: "var z",
                data: [3, 60, 35, 80, 49, 70, 20, 81],
            },
        ],
    });
    return (
        <div className="App">
            <h1>
                <i class="fas fa-user"></i>{" "}
            </h1>
            <div className="row">
                <div className="col-4">
                    <Chart
                        options={state.options}
                        series={state.series}
                        type="bar"
                        width="450"
                    />
                </div>
                <div className="col-4">
                    <Chart
                        options={state.options}
                        series={state.series}
                        type="line"
                        width="450"
                    />
                </div>
                <div className="col-4">
                    <Chart
                        options={state.options}
                        series={state.series}
                        type="area"
                        width="450"
                    />
                </div>
                <div className="col-4">
                    <Chart
                        options={state.options}
                        series={state.series}
                        type="radar"
                        width="450"
                    />
                </div>
                <div className="col-4">
                    <Chart
                        options={state.options}
                        series={state.series}
                        type="histogram"
                        width="450"
                    />
                </div>
                <div className="col-4">
                    <Chart
                        options={state.options}
                        series={state.series}
                        type="scatter"
                        width="450"
                    />
                </div>
                <div className="col-4">
                    <Chart
                        options={state.options}
                        series={state.series}
                        type="heatmap"
                        width="450"
                    />
                </div>
            </div>
        </div>
    );
};

export default BeehiveView;