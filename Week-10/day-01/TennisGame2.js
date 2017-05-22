var TennisGame2 = function() {
    this.P1point = 0;
    this.P2point = 0;
    this.standing = "";
};

TennisGame2.prototype.wonPoint = function(player) {
  if (player === "player1") {
    this.P1point++;
  } else {
    this.P2point++;
  }
};

TennisGame2.prototype.getScore = function() {
  var scoreArray = ["Love", "Fifteen", "Thirty", "Forty"]
  if (this.P1point === this.P2point && this.P1point < 3) {
    this.standing = scoreArray[this.P1point] + '-All';
  } else if (this.P1point === this.P2point && this.P1point > 2) {
    this.standing = "Deuce";
  } else {
    this.standing = scoreArray[this.P1point] + "-" + scoreArray[this.P2point];
    if (this.P1point > 2 && this.P2point > 2) {
      this.scoreAnalyzer(this.P1point, this.P2point);
    }
  }
  return this.standing;
};

TennisGame1.prototype.scoreAnalyzer = function (score1, score2) {
  let gamer = '';
  if (score1 > score2) {
    gamer = '1'
  } else {
    gamer = '2';
  }
  if (Math.abs(score1 - score2) === 1) {
    this.standing = "Advantage player" + gamer;
  } else {
    this.standing = "Win for player" + gamer;
  }
  return this.standing;
}


module.exports = TennisGame2;
