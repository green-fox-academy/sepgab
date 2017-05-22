var TennisGame2 = function() {
    this.P1point = 0;
    this.P2point = 0;
};

TennisGame2.prototype.getScore = function() {
    var score = "";
    var scoreArray = ["Love", "Fifteen", "Thirty", "Forty"]

    if (this.P1point === this.P2point && this.P1point < 3) {
      score = scoreArray[this.P1point] + '-All';
    } else if (this.P1point === this.P2point && this.P1point > 2) {
      score = "Deuce";
    } else {
      score = scoreArray[this.P1point] + "-" + scoreArray[this.P2point];
    }

    if (this.P1point > this.P2point && this.P2point >= 3) {
        score = "Advantage player1";
    }

    if (this.P2point > this.P1point && this.P1point >= 3) {
        score = "Advantage player2";
    }

    if (this.P1point >= 4 && this.P2point >= 0 && (this.P1point - this.P2point) >= 2) {
        score = "Win for player1";
    }
    if (this.P2point >= 4 && this.P1point >= 0 && (this.P2point - this.P1point) >= 2) {
        score = "Win for player2";
    }
    return score;
};

TennisGame2.prototype.SetP1Score = function(number) {
    var i;
    for (i = 0; i < number; i++) {
        this.P1Score();
    }
};

TennisGame2.prototype.SetP2Score = function(number) {
    var i;
    for (i = 0; i < number; i++) {
        this.P2Score();
    }
};

TennisGame2.prototype.P1Score = function() {
    this.P1point++;
};

TennisGame2.prototype.P2Score = function() {
    this.P2point++;
};

TennisGame2.prototype.wonPoint = function(player) {
    if (player === "player1")
        this.P1Score();
    else
        this.P2Score();
};

module.exports = TennisGame2;
