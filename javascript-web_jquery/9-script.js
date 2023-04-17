$(() => {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: data => {
      $('div#hello').text(data.hello);
    },
    error: error => {
      console.log(error);
    }
  });
});
