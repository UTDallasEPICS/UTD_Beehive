import React, { useState } from "react";
import "./Sidebar.css";
import Logo from "../imgs/logo.png";
import { UilSignOutAlt } from "@iconscout/react-unicons";
import { SidebarData, Navigate } from "../Data/Data";
import { UilBars } from "@iconscout/react-unicons";
import { motion } from "framer-motion";
import {Link} from "react-router-dom";

const Sidebar = () => {
  const [selected, setSelected] = useState(0);

  const [expanded, setExpaned] = useState(true)

  const sidebarVariants = {
    true: {
      left : '0'
    },
    false:{
      left : '-60%'
    }
  }
  return (
    <>
      <div className="bars" style={expanded?{left: '60%'}:{left: '5%'}} onClick={()=>setExpaned(!expanded)}>
        <UilBars />
      </div>
    <motion.div className='sidebar'
    variants={sidebarVariants}
    animate={window.innerWidth<=768?`${expanded}`:''}
    >

      <div className="logo">

        <span>
          <span>UTD </span>Beehive
        </span>
      </div>

      <div className="menu">



        {SidebarData.map((item, index) => {
          return (
            <div
              className={selected === index ? "menuItem active" : "menuItem"}
              key={index}
              onClick={() => setSelected(index)}



            >
              <Link to={"/beehive"}></Link>
              <span ><h3 >{item.Dashboard}</h3></span>
              <span className={"beehives"}>{item.heading}</span>
            </div>
          );
        })}

        <div className="menuItem">

        </div>
      </div>
    </motion.div>
    </>
  );
};

export default Sidebar;
