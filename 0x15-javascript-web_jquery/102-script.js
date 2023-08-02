function Hello (language) {
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + language;
  $.get(apiUrl, (content, textStatus) => {
    if (textStatus === 'success') {
      $('DIV#hello').text(content.hello);
    }
  });
}

$(document).ready(function () {
  $('#btn_translate').click(() => {
    const language = $('#language_code').val();
    Hello(language);
  });
});
