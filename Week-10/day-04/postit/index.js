'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mysql = require("mysql");

const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "todos"
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection to todos database established");
});

const app = express();

app.use(bodyParser.json());
app.use(cors());
app.use(express.static(__dirname + '/postit_frontend'));
app.use('/assets/', express.static('assets'));

app.get('/', function(req, res){
  res.sendFile(__dirname + '/postit_frontend/index.html');
});


app.get('/todos', function get(req, res){
  let result = [];
  const query = "SELECT * FROM tasklist";
  conn.query(query, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      rows.forEach(row => {
        result.push(row);
      });
    }
    console.log(result);
    res.send(result);
  });
});

app.get('/todos/:id', function get(req, res){
  let task_id = req.params.id;
  let result = [];
  const query = "SELECT * FROM tasklist WHERE ID = '" + task_id + "';";
  conn.query(query, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      rows.forEach(row => {
        result.push(row);
      });
    }
    console.log(result);
    res.send(result);
  });
});

app.post('/todos', function get(req, res){
  const query1 = "INSERT INTO tasklist (title, status) VALUES ('" + req.body.title + "', '" + req.body.status + "');";
  let result = [];
  conn.query(query1, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      const query2 = "SELECT * FROM tasklist";
      conn.query(query2, function(err,rows){
        if(err) {
          console.log("PARA", err.toString());
          return;
        } else {
          rows.forEach(row => {
            result.push(row);
          });
        }
        console.log(result);
        res.send(result);
      });
    }
  });
})


app.put('/todos/:id', function get(req, res){
  let task_id = req.params.id;
  let result = [];
  const query = "UPDATE tasklist SET status = '" + req.body.status + "' WHERE ID = '" + task_id + "';";
  conn.query(query, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      const query2 = "SELECT * FROM tasklist";
      conn.query(query2, function(err,rows){
        if(err) {
          console.log("PARA", err.toString());
          return;
        } else {
          rows.forEach(row => {
            result.push(row);
          });
        }
        console.log(result);
        res.send(result);
      });
    }
  });
})

app.delete('/todos/:id', function get(req, res){
  let task_id = req.params.id;
  let result = [];
  const query = "DELETE FROM tasklist WHERE ID = '" + task_id + "';";
  conn.query(query, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      const query2 = "SELECT * FROM tasklist";
      conn.query(query2, function(err,rows){
        if(err) {
          console.log("PARA", err.toString());
          return;
        } else {
          rows.forEach(row => {
            result.push(row);
          });
        }
        console.log(result);
        res.send(result);
      });
    }
  });
})

app.listen(3000, function(){
  console.log( 'Todo server is running');
});
