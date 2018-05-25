define([
  'jquery',
], function (
    $
) {
  'use strict';
  var self = {};
  self.ready = false;

  self.setReadyStateFn = function () {
    return function () {
      self.ready = true;
      clearTimeout(self.timeout);
      self.disableBindings();
      $("html").addClass("show-time");
      $(document).trigger("showtime");
    };
  };

  self.enableBindings = function () {
    return $(window).on("load.showtime", self.setReadyStateFn());
  };

  self.disableBindings = function () {
    return $(window).off("load.showtime");
  };

  return {
    initialize: function () {
      self.ready = false;
      self.enableBindings();
      self.timeout = setTimeout(
        self.setReadyStateFn(),
        500
      );
    },
  };
});
