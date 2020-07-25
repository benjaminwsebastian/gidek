jQuery(document).ready(function ($) {
  $(".clickable-row").click(function () {
    window.location = $(this).data("href");
  });
});

$(function () {
  $('#datetimepicker1').datetimepicker({
    format: 'L',
    locale: 'tr'
  });
});