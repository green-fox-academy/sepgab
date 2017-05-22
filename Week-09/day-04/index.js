'use strict';
const mysql = require("mysql");
const express = require('express');
const fs = require('fs');
const parse = require('csv-parse');

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

// const country = 'USA';
// const city = 'Atlanta'
// // const query = "SELECT * FROM author WHERE country = ? AND home_city = ?"
// // conn.query(query, [country, city], function(err,rows){
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
  const query1 = "SELECT book_name FROM book_mast";
  var result = '<ul>';
  conn.query(query1, function(err,rows){
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

app.get('/books/', function get(req, res) {
  var category = req.query.category;
  var publisher = req.query.publisher;
  var plt = req.query.plt;
  var pgt = req.query.pgt;

  var queryFilter = 'SELECT book_name, a.aut_name, c.cate_descrip, p.pub_name, book_price FROM book_mast JOIN author as a ON book_mast.aut_id = a.aut_id JOIN category as c ON book_mast.cate_id = c.cate_id JOIN publisher as p ON book_mast.pub_id = p.pub_id';
  if ((category) || (publisher) || (plt) || (pgt)) {
    queryFilter += ' WHERE'
    if (category) {
      queryFilter += ' cate_descrip = "' + category + '" AND';
    };
    if (publisher) {
      queryFilter += ' pub_name = "' + publisher + '" AND';
    };
    if (plt) {
      queryFilter += ' book_price < "' + plt + '" AND';
    };
    if (pgt) {
      queryFilter += ' book_price > "' + pgt + '" AND';
    };
    queryFilter = queryFilter.slice(0, -4);
  }

  conn.query(queryFilter, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      var result = '<table><tr><td>Book title</td><td>Author name</td><td>Category</td><td>Publisher</td><td>Price</td></tr>';
      rows.forEach(row => {
        result += '<tr><td> ' + row.book_name + '</td><td>' + row.aut_name + '</td><td>' + row.cate_descrip + '</td><td>' + row.pub_name + '</td><td>' + row.book_price + '</td></tr>';
      });
      result += '</table>';
    }
    res.send(result);
  });
});


app.listen( 3000, function() {
  console.log('server running');
})



var csvData=[];
fs.createReadStream(req.file.path)
    .pipe(parse({delimiter: ':'}))
    .on('data', function(csvrow) {
        console.log(csvrow);
        //do something with csvrow
        csvData.push(csvrow);
    })
    .on('end',function() {
      //do something wiht csvData
      console.log(csvData);
    });



// conn.end();
