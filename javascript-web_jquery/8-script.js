$(() => {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    type: 'GET',
    contentType: 'application/json',
    success: data => {
      for (const film of data.results) {
        $('ul#list_movies').append(`<li>${film.title}</li>`);
      }
    },
    error: error => {
      console.log(error);
    }
  });
});
