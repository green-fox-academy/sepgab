'use strict';

const mysql = require("mysql");
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "reddit_posts"
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.use(bodyParser.json());
app.use(cors());

// app.get('/', function(req, res){
//   res.sendFile(__dirname + '/index.html');
//   // app.use('/assets/', express.static('assets'));
// });

app.get('/posts', function get(req, res){
  const queryGet = "SELECT * FROM posts";
  let result = {"posts": 0};
  conn.query(queryGet, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      result.posts = rows;
    }
    res.json(result);
  });
});

app.post('/posts', function get(req, res){
  const queryPost = "INSERT INTO posts (href, title) VALUES ('" + req.body.href + "', '" + req.body.title + "');";
  let result = {"posts": 0};
  conn.query(queryPost, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      result.posts = rows;
    }
    res.json(result);
  });
})

app.put('/posts/<id>/upvote', function get (req, res) {
  let fullUrl = document.URL;
  let urlArray = fullUrl.split('/');
  let postID = urlArray[urlArray.length-2];
  let currentScore =
  const queryUpvote = 'UPDATE posts SET score = score + 1 WHERE id = "' + postID + '";'
  
})


app.listen(3000, function(){
  console.log( 'Server is running');
});
