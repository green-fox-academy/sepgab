var score = "";

var TennisGame1 = function(player1Name, player2Name) {
  this.m_score1 = 0;
  this.m_score2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame1.prototype.wonPoint = function(playerName) {
  if (playerName === "player1") {
    this.m_score1++;
  } else {
    this.m_score2++;
  }
};

TennisGame1.prototype.getScore = function() {
  if (this.m_score1 !== this.m_score2) {
    score = setScore(this.m_score1) + "-" + setScore(this.m_score2);
    if (this.m_score1 >= 4 || this.m_score2 >= 4) {
      winAnalyzer(this.m_score1, this.m_score2);
    }
  } else {
    if (this.m_score1 > 2) {
      score = "Deuce";
    } else {
      score = setScore(this.m_score1) + "-All";
    }
  }

  return score;
};

var setScore = function(tempScore) {
  score = "";
  switch (tempScore) {
    case 0:
    score += "Love";
    break;
    case 1:
    score += "Fifteen";
    break;
    case 2:
    score += "Thirty";
    break;
    case 3:
    score += "Forty";
    break;
  }
  return score;
}
var winAnalyzer = function (score1, score2) {
  let player = '';
  if (score1 > score2){
    player = '1'
  } else {
    player = '2';
  }
  if (Math.abs(score1 - score2) === 1) {
    score = "Advantage player" + player;
  } else {
    score = "Win for player" + player;
  }
  return score;
}

module.exports = TennisGame1;
