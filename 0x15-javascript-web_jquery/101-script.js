// This script shall add remove and clear elem from lst upon click

$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list LI').last().remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
