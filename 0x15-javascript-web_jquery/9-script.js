// This script shall get hello from API link

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
