const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();

//Enable cors and bodyParser so requests can come through
app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(bodyParser.json());

app.use(cors({
    credentials: true,
}));

app.use(express.static(__dirname + "/"));

// Routes
app.get('/', function(req, res) {
    res.status(200).send("Hello World");
});

app.get('/dataVis', function(req, res){
    res.status(200).sendFile(__dirname + "/index.html");
})

var port = process.env.PORT || 8080;

app.listen(port, () => console.log('Server listening on port: ' + port));