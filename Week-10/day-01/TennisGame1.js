var TennisGame1 = function() {
  this.playerScore1 = 0;
  this.playerScore2 = 0;
  this.standing = '';
};

TennisGame1.prototype.wonPoint = function(playerName) {
  if (playerName === "player1") {
    this.playerScore1++;
  } else {
    this.playerScore2++;
  }
};

TennisGame1.prototype.getScore = function() {
  if (this.playerScore1 !== this.playerScore2) {
    this.standing = this.setScore(this.playerScore1) + "-" + this.setScore(this.playerScore2);
    if (this.playerScore1 >= 4 || this.playerScore2 >= 4) {
      this.scoreAnalyzer(this.playerScore1, this.playerScore2);
    }
  } else {
    if (this.playerScore1 > 2) {
      this.standing = "Deuce";
    } else {
      this.standing = this.setScore(this.playerScore1) + "-All";
    }
  }
  return this.standing;
};

TennisGame1.prototype.setScore = function(currentScore) {
  let scoreArray = ["Love", "Fifteen", "Thirty", "Forty"]
  this.standing = scoreArray[currentScore];
  return this.standing;
}

TennisGame1.prototype.scoreAnalyzer = function (score1, score2) {
  let player = '';
  if (score1 > score2){
    player = '1'
  } else {
    player = '2';
  }
  if (Math.abs(score1 - score2) === 1) {
    this.standing = "Advantage player" + player;
  } else {
    this.standing = "Win for player" + player;
  }
  return this.standing;
}

module.exports = TennisGame1;
