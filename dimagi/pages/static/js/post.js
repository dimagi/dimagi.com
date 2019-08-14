requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
  }
});

require([
  'jquery',
], function (
  $
) {
  'use strict';
  if ($(document).ready(function (e) {
    $('.easy-footnote a[title]').each(function () {
      var oldUrl = $(this).attr("title"); // Get current title
      var newUrl = oldUrl.replace(/<[ap]\b[^>]*>|<\/[ap]>/g, ""); // Create new title
      $(this).attr("title", newUrl); // Set title value
    });
  }));
});
