function Hello (language) {
  $.get('https://fourtonfish.com/hellosalut/', (content, textStatus) => {
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
