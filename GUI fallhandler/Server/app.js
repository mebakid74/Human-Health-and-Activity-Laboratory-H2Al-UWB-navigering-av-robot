const express = require('express')
const app = express();
const port = process.env.PORT || 5000;
const path = require('path')
app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header(
        "'Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS'"
    );
    res.header(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, X-Auth-Token, Content-Type, Accept"
    );
    next();
});

app.use(express.static('public'));

app.get("/", function(req, res){
    res.sendFile(path.join(__dirname, './public/html/index.html'));
});

app.get("/home", function(req, res){
    res.sendFile(path.join(__dirname, './public/html/main.html'));
});

const server = app.listen(port, () => {
    console.log("Listening on port: " + port);
});
