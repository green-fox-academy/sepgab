'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an balance of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - balance
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function balance(account) {
  accounts.forEach(function(el) {
    if (el.account_number === account) {
      console.log('Name:', el.client_name, ', Balance:', el.balance)
    }
  })
}

balance(23456311);

function transfer(from, to, sum) {
  var validate = false;
  for (var num1 = 0; num1 < accounts.length; num1++) {
    for (var num2 = 0; num2 < accounts.length; num2++) {
      if (accounts[num1].account_number === from && accounts[num2].account_number === to && accounts[num1].balance >= sum) {
        accounts[num1].balance -= sum;
        accounts[num2]. balance += sum;
        validate = true;
      }
    }
  }
  if (validate === false) {
    console.log( '404 - account not found or insufficient balance' );
  }
}

balance(11234543);
balance(43546731);
transfer(11234543, 43546731, 2000)
balance(11234543);
balance(43546731);
