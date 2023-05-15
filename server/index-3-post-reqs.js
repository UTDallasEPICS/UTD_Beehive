// Boilerplate code start
const express = require("express");
const pool = require("./db");
const path = require("path");
var cors = require("cors");

const app = express();

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

//  ---------------------------------------------------------------------------------------------------

app.get("/databaseDataWeight", async (req, res) => {
  try {
    const allTodos = await pool.query("SELECT * FROM weightTable");
    res.json(allTodos.rows);
  } catch (err) {
    console.error(err.message);
  }
});

// POST request to put weight data into database
app.post("/databaseDataWeight", async (req, res) => {
  try {
    console.log("/databaseDataWeight Called()");
    const { weight } = req.body;
    console.log("{ weight }", weight);
    const newValue1 = await pool.query(
      "INSERT INTO weightTable (testdata) VALUES($1) RETURNING *",
      [weight]
    );

    res.json({"weight": newValue1.rows[0]});
  } catch (err) {
    console.error(err.message);
  }
});

app.delete("/databaseDataWeight/:id", async (req, res) => {
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


// -----------------------------------------------------------------------------------------------------------------
app.get("/databaseDataTemp", async (req, res) => {
  try {
    const allTodos = await pool.query("SELECT * FROM temperatureTable");
    res.json(allTodos.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.post("/databaseDataTemp", async (req, res) => {
  try {
    console.log("/databaseDataTemp Called()");
    const { temp } = req.body;
    console.log("{ temp }", temp);
    const newValue2 = await pool.query(
      "INSERT INTO temperatureTable (testdata) VALUES($1) RETURNING *",
      [temp]
    ); 

    res.json({"temp": newValue2.rows[0]});
  } catch (err) {
    console.error(err.message);
  }
});

app.delete("/databaseDataTemp/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const deleteTodo = await pool.query(
      "DELETE FROM temperatureTable WHERE weightid = $1",
      [id]
    );
    res.json("value deleted!");
  } catch (err) {
    console.log(err.message);
  }
});

// -----------------------------------------------------------------------------------------------------------------
app.get("/databaseDataHumidity", async (req, res) => {
  try {
    const allTodos = await pool.query("SELECT * FROM humidityTable");
    res.json(allTodos.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.post("/databaseDataHumidity", async (req, res) => {
  try {
    console.log("/databaseDataHumidity Called()");
    const { humidity } = req.body;
    console.log("{ humidity }", humidity);
    const newValue3 = await pool.query(
      "INSERT INTO humidityTable (testdata) VALUES($1) RETURNING *",
      [humidity]
    ); 

    res.json({"humidity": newValue3.rows[0]});
  } catch (err) {
    console.error(err.message);
  }
});

app.delete("/databaseDataHumidity/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const deleteTodo = await pool.query(
      "DELETE FROM humidityTable WHERE weightid = $1",
      [id]
    );
    res.json("value deleted!");
  } catch (err) {
    console.log(err.message);
  }
});



// ----------------------------------------------------------------------------------------------------------

app.use(express.static(path.join(__dirname, "/views")));

app.get("*", function (req, res) {
  res.sendFile(path.join(__dirname, "/views", "index.html"));
});

app.listen(5001, () =>
  console.log("Server running on PORT: 5001 @ http://localhost:5001")
);
