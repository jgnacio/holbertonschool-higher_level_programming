$(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    contentType: 'application/json',
    success: data => {
      $('div#character').text(data.name);
    },
    error: error => {
      console.log(error);
    }
  });
});
