// this script shall add lst of elem when user click tag

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
