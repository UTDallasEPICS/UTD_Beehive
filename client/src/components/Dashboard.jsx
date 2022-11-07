import '../App.css'
import React, {useState} from "react";
import Chart from "react-apexcharts";
import MainDash from "./MainDash/MainDash";
import RightSide from "./RigtSide/RightSide";

const Dashboard = () => {

    return (<>
            <MainDash/>
            <RightSide/>
        </>

    );
};

export default Dashboard;