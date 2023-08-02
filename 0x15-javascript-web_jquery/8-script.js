$.get('https://swapi-api.hbtn.io/api/films/?format=json', (content, textStatus) => {
  if (textStatus === 'success') {
    for (const movie of content.results) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    }
  }
});
