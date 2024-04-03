// This script shall get lst of all movies using api link
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $(data.results).each(function (index, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
