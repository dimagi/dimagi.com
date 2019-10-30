define([
  'jquery',
], function (
    $
) {
  'use strict';
  var self = {};

  self.activate = function () {
    self.$banner.slideDown();
  };

  self.deactivate = function () {
    self.$banner.slideUp();
  };

  self.enableBindings = function () {
    $('.top-banner-ad-close').click(function () {
      self.deactivate();
    });
  };

  return {
    initialize: function () {
      self.$banner = $(".top-banner-ad");
      if (self.$banner) {
        self.activate();
        self.enableBindings();
      }
    }
  };
});
