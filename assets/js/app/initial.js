define([
  'jquery',
], function (
  $
) {
  'use strict';

  return {
    initialize: function () {
      var ua = navigator.userAgent,
      iOS = /iPad|iPhone|iPod/.test(ua),
      iOS11 = /OS 11_0|OS 11_1|OS 11_2/.test(ua),
      $stylesheet = $('#js-async-stylesheets'),
      styleLinks = $stylesheet.text();

      // ios 11 bug caret position
      if ( iOS && iOS11 ) {
        // Add CSS class to body
        $("html").addClass("ios-modal-fix");
      }

      // load async styles
      styleLinks = styleLinks.substring(1, styleLinks.length - 1);
      $stylesheet.before(styleLinks);

    },
  };
});
