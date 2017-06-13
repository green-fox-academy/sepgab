var tape = require('tape');
var mysql = require('mysql');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '',
  database : 'test'
});

connection.connect();

function getAllMessage(callback) {
	connection.query('SELECT * FROM hello', function (error, results, fields) {
		if (error) throw error;
		callback(results);
	});
	connection.end();
}

tape('timing test', function (t) {
	getAllMessage( results => {
		t.equal(results.length, 0);
		t.end();
	})
});
