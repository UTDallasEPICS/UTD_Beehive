import "./styles.css";
import React, { useEffect, useState } from 'react';import axios from "axios"
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend
} from "recharts";


export default function App() {
    const [weightData, setWeightData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const res = await fetch("http://172.20.10.12:3000/data");
            const data = await res.json();
            console.log(data);

            let i = 0;
            let dataArray = [];

            while (i < data.length) {
                console.log(data[i]);
                dataArray.push({"weight": data[i], "time": "time"})
                i++;
            }

            setWeightData(dataArray);
        };
        fetchData();
    }, []);

    return (
        <LineChart
            width={1100}
            height={800}
            data={weightData}
            margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5
            }}
        >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line
                type="monotone"
                dataKey="weight"
                stroke="#8884d8"
                activeDot={{ r: 8 }}
            />
        </LineChart>
    );
}

///--------------------------------

