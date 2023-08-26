// Last updated 4 May 2023



// Boilerplate code start
const express = require("express");
const pool = require("./db");
const path = require("path");
var cors = require("cors");

const app = express();


/*
app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "*");
  res.setHeader("Access-Control-Allow-Headers", "*");
  res.setHeader("Access-Control-Allow-Credentials", true);
  next();
});


app.use(
  cors({
    origin: "http://localhost:3000",
    methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
    credentials: true,
  })
);
*/

app.use(cors(
{
  origin: "http://10.159.180.198:3000", // rebecca's machine IP address
  optionsSuccessStatus: 200
}));

app.use(express.json());

// Boilerplate code end

const allData = [];

// Get request to ESP32
app.get("/data", (req, res) => {
  console.log("Hello from /data API");
  return res.json(allData);
});

// Don't really need this because we already have a GET request for data from the ESP32
app.post("/data", (req, res) => {
  const value = req.body;

  const data = {
    value,
  };

  allData.push(value.x);
  return res.json(value);
});


// GET request from website to send weight data
app.get("/databaseDataWeight", async (req, res) => {
  try {
    console.log("\n /databaseDataWeight GET Request called!");
    const allTodos = await pool.query("SELECT * FROM weightTable");
    // console.log(allTodos.rows[0]);
    return res.json({ "weightData": allTodos.rows });
  } catch (err) {
    console.error(err.message);
  }
});

// GET request from website to send temp data
app.get("/databaseDataTemp", async (req, res) => {
  try {
    console.log("\n /databaseDataTemp GET Request called!");
    const allTodos = await pool.query("SELECT * FROM temperatureTable");
    // console.log(allTodos.rows[0]);
    return res.json({ "tempData": allTodos.rows });
  } catch (err) {
    console.error(err.message);
  }
});

// GET request from website to send humidity data
app.get("/databaseDataHumidity", async (req, res) => {
  try {
    console.log("\n /databaseDataHumidity GET Request called!");
    const allTodos = await pool.query("SELECT * FROM humidityTable");
    // console.log(allTodos.rows[0]);
    return res.json({ "humidityData": allTodos.rows });
  } catch (err) {
    console.error(err.message);
  }
});




// POST request to put data into database
app.post("/databaseData", async (req, res) => {
  try {
    console.log("/databaseData Called()");
    const { weight, temp, humidity } = req.body;
    console.log("{ w, t, h }", weight, temp, humidity);
    const newValue1 = await pool.query(
      "INSERT INTO weightTable (testdata) VALUES($1) RETURNING *",
      [weight]
    );
   const newValue2 = await pool.query(
      "INSERT INTO temperatureTable (testdata) VALUES($1) RETURNING *",
      [temp]
    );  

   const newValue3 = await pool.query(
      "INSERT INTO humidityTable (testdata) VALUES($1) RETURNING *",
      [humidity]
    );  


    res.json({"weight": newValue1.rows[0], "temp": newValue2.rows[0], "humidity": newValue3.rows[0]});
  } catch (err) {
    console.error(err.message);
  }
});

app.delete("/databaseData/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const deleteTodo = await pool.query(
      "DELETE FROM weightTable WHERE weightid = $1",
      [id]
    );
    res.json("value deleted!");
  } catch (err) {
    console.log(err.message);
  }
});

app.use(express.static(path.join(__dirname, "/views")));

app.get("*", function (req, res) {
  res.sendFile(path.join(__dirname, "/views", "index.html"));
});

app.listen(5008, () =>
  console.log("Server running on PORT: 5008 @ http://localhost:5008")
);
