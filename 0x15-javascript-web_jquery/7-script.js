$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (content, textStatus) => {
  if (textStatus === 'success') {
    $('DIV#character').text(content.name);
  }
});
