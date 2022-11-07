// Sidebar imports
import {
  UilEstate,
  UilClipboardAlt,
  UilUsersAlt,
  UilPackage,
  UilChart,
  UilSignOutAlt,
} from "@iconscout/react-unicons";

// Analytics Cards imports
import { UilUsdSquare, UilMoneyWithdrawal } from "@iconscout/react-unicons";

// Recent Card Imports
import img1 from "../imgs/img1.png";
import img2 from "../imgs/img2.png";
import img3 from "../imgs/img3.png";

// Sidebar Data
export const Navigate = [
  {
    heading: "Dashboard",
  },
];

export const SidebarData = [
  {Dashboard: "Dashboard",},
  {heading: "Beehive 1",},
  {heading: "Beehive 2",},
  {heading: "Beehive 3",},
  {heading: 'Beehive 4'},
  {heading: 'Beehive 5'},
  {heading: 'Beehive 6'},
  {heading: 'Beehive 7'},
  {heading: 'Beehive 8'},
];

// Analytics Cards Data
export const cardsData = [
  {
    title: "Weight",
    color: {
      backGround: "linear-gradient(180deg, #bb67ff 0%, #c484f3 100%)",
    },
    barValue: 70,
    value: "70",
    png: UilUsdSquare,
    series: [
      {
        name: "Weight",
        data: [31, 40, 44, 51, 52, 64, 70],
      },
    ],
  },
  {
    title: "Temperature",
    color: {
      backGround: "linear-gradient(180deg, #FF919D 0%, #FC929D 100%)",
      boxShadow: "0px 10px 20px 0px #FDC0C7",
    },
    barValue: 80,
    value: "40",
    png: UilMoneyWithdrawal,
    series: [
      {
        name: "Temperature",
        data: [10, 100, 50, 70, 80, 30, 40],
      },
    ],
  },
  {
    title: "Humidity",
    color: {
      backGround:
        "linear-gradient(rgb(248, 212, 154) -146.42%, rgb(255 202 113) -46.42%)",
      boxShadow: "0px 10px 20px 0px #F9D59B",
    },
    barValue: 60,
    value: "93",
    png: UilClipboardAlt,
    series: [
      {
        name: "Humidity",
        data: [70, 75, 65, 89, 90, 80, 93],
      },
    ],
  },
];

// Recent Update Card Data
export const UpdatesData = [
  {
    name: "Server",
    noti: "is under maintenance, it is currently not receiving requests. ",
    time: "17 hours ago",
  },
  {
    name: "Beehive 3",
    noti: "has disconnected. The data input is currently paused.",
    time: "2 days ago",
  },
  {
    name: "Solar Panel",
    noti: "has reached battery capacity",
    time: "8 days ago",
  },
  {
    name: "Beehive 1",
    noti: "is connected. Data is being sent to server",
    time: "12 days ago",
  },
  {
    name: "Beehive 2",
    noti: "sensors are not sending data",
    time: "12 days ago",
  },
];


