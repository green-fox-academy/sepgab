'use strict';

const mysql = require("mysql");
const fs = require('fs');
const mm = require('musicmetadata');

const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "audio_player"
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection to audio database established");
});

const root = "C://Users/sepler.gabor.TARNA3/Desktop/GreenFox/sepgab/Week-10/day-02/audio_backend/frontend/assets/music/"

const loadDatabase = function(tableName, dirname, callback) {
  let query = 'TRUNCATE TABLE ' + tableName + ';';
  conn.query(query, function(err){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      console.log('Tracks table erased');
      callback(dirname);
    }
  });
}

const readFiles = function(dirname) {
  fs.readdir(dirname, function(err, filenames) {
    if (err) {
      onError(err);
      return;
    }
    filenames.forEach(function(filename) {
      let readableStream = fs.createReadStream(dirname + filename);
      let parser = mm(readableStream, { duration: true }, function (err, metadata) {
        if (err) throw err;
        readableStream.close();
        writeDatabase(filename, metadata);
      });
    });
  });
}

const writeDatabase = function(filename, metadata) {
  let query = 'INSERT INTO tracks (title, artist, duration, path) VALUES ("' + metadata.title + '", "' + metadata.artist + '", "' + metadata.duration + '", "' + filename + '");';
  conn.query(query, function(err){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      console.log('Track added to database');
    }
  });
}

loadDatabase('tracks', root, readFiles);

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

app.use(bodyParser.json());
app.use(cors());

app.use(express.static(__dirname + '/frontend'));
app.use('/music/', express.static('assets/music'));

app.get('/', function(req, res){
  res.sendFile(__dirname + '/frontend/audio.html');
  app.use('/assets/', express.static('assets'));
});

app.get('/playlists', function get(req, res){
  // let result = [
  // 	{ "id": 1, "title": "Favorites", "system": 1},
  // 	{ "id": 2, "title": "Music for programming", "system": 0},
  // 	{ "id": 3, "title": "Driving", "system": 0},
  // 	{ "id": 5, "title": "Fox house", "system": 0},
  // ]
  let result = [];
  const query = "SELECT * FROM playlists";
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

app.get('/playlist-tracks', function get(req, res){
  // let result = [
  //   { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
  //   { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
  // ]
  let result = [];
  const query = "SELECT * FROM tracks";
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

app.get('/playlist-tracks/:playlist_id', function get(req, res){
  let playlist_id = req.params.playlist_id;
  let tracklist = [];
  let result = [];
  // if (playlist_id === '1') {
  //   result = [
  //     { "id": 1, "title": "Enter Sandman", "artist": "Metallica", "duration": 332, "path": root + "01. Enter Sandman.mp3" },
  //   ]
  // } else {
  //   console.log('No such playlist!');
  // }
  const query1 = "SELECT tracklist FROM playlists WHERE pID = '" + playlist_id + "';";
  conn.query(query1, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      tracklist = rows[0].tracklist.split('tID');
      tracklist.shift();
    }
    let filter = '';
    for (let i = 0; i < tracklist.length; i++) {
      filter += parseInt(tracklist[i]) + " || tID = ";
    }
    filter = filter.slice(0, -10);
    const query2 = "SELECT * FROM tracks WHERE tID = " + filter + ";";
    conn.query(query2, function(err,rows){
      if(err) {
        console.log("PARA", err.toString());
        return;
      } else {
        rows.forEach(row => {
          result.push(row);
        });
      }
      res.send(result);
    });
  });
});

app.post('/playlists', function get(req, res){
  const query1 = "INSERT INTO playlists (title) VALUES ('" + req.body.title + "');";
  let result = [];
  conn.query(query1, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      const query2 = "SELECT * FROM playlists";
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

app.post('/playlist-tracks/:playlist_id', function get(req, res){
  let playlist_id = req.params.playlist_id;
  console.log(playlist_id);
  const query1 = "SELECT tracklist FROM playlists WHERE pID = '" + playlist_id + "';";
  console.log(query1);
  let result = [];
  conn.query(query1, function(err,rows){
    if(err) {
      console.log("PARA", err.toString());
      return;
    } else {
      rows.forEach(row => {
        result.push(row);
      });
      console.log(result);
      let normalizedResult = '';
      console.log(result[0].tracklist);
      if (result[0].tracklist === null || result[0].tracklist === '') {
        normalizedResult = '';
      } else {
        normalizedResult = result[0].tracklist;
      }
      console.log(normalizedResult);
      let updatedResult = ''
      updatedResult += normalizedResult + 'tID' + req.body.tID.toString();
      console.log(updatedResult);
      const query2 = "UPDATE playlists SET tracklist = '" + updatedResult + "' WHERE pID = '" + playlist_id + "';";
      // const query2 = "INSERT INTO playlists (tracklist) VALUES ('" + updatedResult + "' WHERE pID = '" + playlist_id + "';";
      console.log(query2);
      result = [];
      conn.query(query2, function(err){
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
  console.log( 'Audio server is running');
});
