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

  $('#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13) {
      const language = $('#language_code').val();
      Hello(language);
    }
  });
});
