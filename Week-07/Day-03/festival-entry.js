'use strict';

var watchlist = []

var security_alchol_loot = 0

var queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

// Queue of festivalgoers at entry
// no. of alcohol units
// no. of guns

// Create a security_check function that returns a list of festivalgoers who can enter the festival

// If guns are found, remove them and put them on the watchlist (only the names)
// If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

function securityCheck() {
  var entryList = [];
  var watchList = [];
  var alcoholLoot = 0;
  queue.forEach(function(el) {
    if (el.guns === 1) {
      el.guns = 0;
      watchList.push(el.name);
    } else {
      if (el.alcohol > 0) {
        alcoholLoot += el.alcohol;
        el.alcohol = 0;
      }
      entryList.push(el.name);
    }
  })
  console.log( 'They can enter:', entryList );
  console.log( 'Watchlist:', watchList );
  console.log( 'Security alcohol loot:', alcoholLoot );
}

securityCheck();
