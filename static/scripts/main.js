$(document).ready(setup);

const alreadyProcessed = new Set();
let word = "";
let remaining = 7;
let score = 0;
let best = 0;
let playing = true;

function setup () {
  word = $('#word-data').data('word');

  if (localStorage.pwdSolverBest) {
    best = Number(localStorage.pwdSolverBest);
  }
  if (localStorage.pwdSolverScore) {
    score = Number(localStorage.pwdSolverScore);
  }

  $('#current-score').text(score);
  $('#best-score').text(best);

  $('.back-to-landing').click(function () {
    window.location.href = '/';
  });

  $('.key').click(function () {
    if (playing) {
      checkLetter($(this).text());
    }
  });

  $('body').on('keydown', function (event) {
    if (playing && event.which >= 65 && event.which <= 90) {
      checkLetter(String.fromCharCode(event.which));
    }
  });
}

function checkLetter (letter) {
  if (alreadyProcessed.has(letter)) {
    return;
  }

  alreadyProcessed.add(letter);

  if (word.includes(letter)) {
    updateUiCorrect();
  } else {
    updateUiWrong();
    $('.key:contains(' + letter + ')').addClass('wrong');
  }

  $('.key:contains(' + letter + ')').prop('disabled', true);
}

function updateUiCorrect () {
  const wordProgress = [];
  const wordProgressHtml = [];

  for (let i = 0; i < word.length; i++) {
    if (alreadyProcessed.has(word[i])) {
      wordProgress[i] = word[i];
      wordProgressHtml[i] = '<span>' + word[i] + '</span>';
    } else {
      wordProgress[i] = '_';
      wordProgressHtml[i] = '<span>_</span>';
    }
  }

  $('.password-output').html(wordProgressHtml.join(''));

  if (wordProgress.join('') === word) {
    playing = false;

    score += remaining;
    localStorage.pwdSolverScore = score;
    if (score > best) {
      best = score;
      localStorage.pwdSolverBest = best;
    }
    $('#current-score').text(score);
    $('#best-score').text(best);

    $('#success-modal').css('display', 'flex');

    $('#points-earned').text(remaining);

    $('#next-game').click(function () {
      playing = true;
      window.location.reload();
    });
  }
}

function updateUiWrong () {
  remaining--;
  const imgUrl = '/static/images/wrong' + (7 - remaining) + '.svg';

  $('.screen p').text(remaining);
  $('.screen').css('background-image', 'url("' + imgUrl + '")');

  if (remaining === 0) {
    playing = false;

    $('#gameover-modal').css('display', 'flex');

    $('#total-score').text(score);

    $('#play-again').click(function () {
      playing = true;
      score = 0;
      localStorage.pwdSolverScore = 0;
      window.location.reload();
    });
  }
}
