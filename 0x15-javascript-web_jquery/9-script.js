$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (content, textStatus) => {
    if (textStatus === 'success') {
      $('DIV#hello').text(content.hello);
    }
  });
});
