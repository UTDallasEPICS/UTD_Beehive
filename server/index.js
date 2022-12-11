const express = require("express");

const app = express();

app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});


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

app.listen(3000, ('172.20.10.5'));