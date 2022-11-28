const express = require("express");

const app = express();
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

app.listen(3000, ('{PORT}'));