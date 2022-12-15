$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
  var movies = data.results;
  for (var i = 0; i < movies.length; i++) {
    var title = movies[i].title;
    $("ul#list_movies").append("<li>" + title + "</li>");
  }
});
