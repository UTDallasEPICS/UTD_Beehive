const express = require("express");
const pool = require("./db");
const path = require("path");
var cors = require('cors');

const app = express();

app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', '*');
    res.setHeader('Access-Control-Allow-Headers', '*');
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});

app.use(
    cors({
      origin: "http://localhost:3000",
      methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
      credentials: true
    })
  )



app.use(express.json());



const allData= [];

app.get("/data", (req, res) =>{
    return res.json(allData);
})

app.post("/data", (req, res) =>{
    const value = req.body;

    const data = {
        value
    }

    allData.push(value.x);
    return res.json(value)
})


app.get("/databaseData", async (req, res) => {
    try {
        const allTodos = await pool.query("SELECT * FROM weightTable");
        res.json(allTodos.rows);
    } catch (err) {
        console.error(err.message);
    }
});

app.post("/databaseData", async (req, res) => {
    try {
        const { x } = req.body;
        const newValue = await pool.query(
            "INSERT INTO weightTable (value) VALUES($1) RETURNING *",
            [x]
        );

        res.json(newValue.rows[0]);
    } catch (err) {
        console.error(err.message);
    }
});


app.delete("/databaseData/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const deleteTodo = await pool.query("DELETE FROM weightTable WHERE weightid = $1", [
      id
    ]);
    res.json("value deleted!");
  } catch (err) {
    console.log(err.message);
  }
});


app.use(express.static(path.join(__dirname, '/views')));

app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname, '/views', 'index.html'));
});


app.listen(3000, () => console.log("http://localhost:3000"));

