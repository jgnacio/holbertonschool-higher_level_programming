$(() => {
  $('div#toggle_header').click(() => {
    if ($('header').attr('class') === 'red') {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else {
      $('header').addClass('red');
      $('header').removeClass('green');
    }
  });
});
