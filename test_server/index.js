const express = require("express");
const path = require("path");

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

app.use(express.static(path.join(__dirname, '/views')));

app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname, '/views', 'index.html'));
});

app.listen(5000, () => {

});