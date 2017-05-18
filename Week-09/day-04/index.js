'use strict';
const mysql = require("mysql");
const express = require('express');

const app = express()

const conn = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "root",
  database: "bookstore"
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});




const country = 'USA';
const city = 'Atlanta'
// // const query = "SELECT * FROM author WHERE country = ? AND home_city = ?"
// // conn.query(query, [country, city], function(err,rows){
//
const query = "SELECT book_name FROM book_mast"

// conn.query("SELECT * FROM author WHERE country = '" + country + "'", function(err,rows){
// conn.query(query, function(err,rows){
//   if(err) {
//     console.log("PARA", err.toString());
//     return;
//   } else {
//     console.log("Data received from Db:\n");
//     rows.forEach(row => {
//       console.log(row.aut_name)
//     });
//   }
// });

app.get('/booktitles/', function get(req, res) {
  var result = '<ul>';
  conn.query(query, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      rows.forEach(row => {
        result += '<li> ' + row.book_name + '</li>';
      });
      result += '</ul>';
    }
    res.send(result);
  });
});

app.listen( 3000, function() {
  console.log('server running');
})



// conn.end();
