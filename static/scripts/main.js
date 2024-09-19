$(document).ready(setup);

const alreadyProcessed = new Set();
let word = "";
let remaining = 7;
let score = 0;
let best = 0;
let playing = true;
let typeItInst = null;
let achievedBest = false;

function setup () {
  word = $('#word-data').data('word');

  if ($('#feedback').length){
    typeItInst = new TypeIt('#feedback', {
      strings: ['Decryption sequence initiated', 'Awaiting input...'],
      speed: 10,
      cursorChar: "■",
      afterStep: function (instance) {
        $('#feedback').scrollTop($('#feedback').prop('scrollHeight'));
      },
      waitUntilVisible: true
    });

    typeItInst.break().go();
  }

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
    updateUiCorrect(letter);
  } else {
    updateUiWrong(letter);
    $('.key:contains(' + letter + ')').addClass('wrong');
  }

  $('.key:contains(' + letter + ')').prop('disabled', true);
}

function updateUiCorrect (letter) {
  const wordProgress = [];
  const wordProgressHtml = [];
  const feedback = [['Decryption sequence progressing..', `Letter ${letter} confirmed in password`],
                    [`Correct match: ${letter}`, 'Decrypting further...'],
                    ['Security vulnerability exploited', `${letter} validated`]];
  const finalFeedback = ['Access Granted', 'Decryption Complete', 'Welcome, User X']

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

  /* Change cursor color  */
  $(':root')[0].style.setProperty('--ti-cursor-color', '#10D023');

  if (wordProgress.join('') === word) {
    playing = false;

    score += remaining;
    localStorage.pwdSolverScore = score;
    if (score > best) {
      best = score;
      localStorage.pwdSolverBest = best;
      achievedBest = true;
    }
    $('#current-score').text(score);
    $('#best-score').text(best);

    /* Ensure typing is completed synchronously before displaying modal  */
    typeIt(feedback[Math.floor(Math.random() * feedback.length)], "", "", function () {
      typeIt(finalFeedback, "", "", function (){
        $('#success-modal').css('display', 'flex');

        if (achievedBest) {
          $('#new-best').css('visibility', 'visible');
        }

        $('#points-earned').text(remaining);

        $('#next-game').click(function () {
          playing = true;
          window.location.reload();
        });
      });
    });
  } else {
    typeIt(feedback[Math.floor(Math.random() * feedback.length)]);
  }
}

function updateUiWrong (letter) {
  remaining--;
  const feedback = [['Decryption failed', `No match for character ${letter}`, `Remaining attempts: ${remaining}`],
                    [`Decryption error: ${letter} not part of the correct sequence`, `Remaining attempts: ${remaining}`],
                    [`System alert: Failed character input ${letter} not valid`, `Remaining attempts: ${remaining}`]];
  const finalFeedback = ['Unauthorized access detected...', 'System Lockdown Initiated..', 'Shutting down connection...'];

  /* Change cursor color  */
  $(':root')[0].style.setProperty('--ti-cursor-color', '#FF3333');

  if (remaining === 0) {
    playing = false;

    /* Ensure typing is completed synchronously before displaying modal  */
    typeIt(feedback[Math.floor(Math.random() * feedback.length)], "<span class='error-log'>", "</span>", function () {
      typeIt(finalFeedback, "<span class='error-log'>", "</span>", function () {
        $('#gameover-modal').css('display', 'flex');

        $('#total-score').text(score);

        $('#play-again').click(function () {
          playing = true;
          score = 0;
          localStorage.pwdSolverScore = 0;
          window.location.reload();
        });
      });
    });
  } else {
    typeIt(feedback[Math.floor(Math.random() * feedback.length)], "<span class='error-log'>", "</span>");
  }
}

function typeIt(feedbackList, start="", end="", callback=null) {
  typeItInst.break().flush();

  for (let s of feedbackList) {
    if (start){
      s = start + s;
    }

    if (end){
      s = s + end;
    }

    typeItInst.type(s).break();
  }

  typeItInst.flush(callback);
}