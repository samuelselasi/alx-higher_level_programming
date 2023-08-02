$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (content, textStatus) => {
    if (textStatus === 'success') {
      $('DIV#hello').text(content.hello);
    }
  });
});
