define([
  'modernizr',
  'lodash',
  'jquery',
], function (Modernizr, _, $) {
  'use strict';
  var self = {};

  self.enableBindings = function () {
    $(document).on("click", 'a[href^="#"]:not([href="#"]):not([role="tab"])', function (e) {
      self.scrollTo(e);
    });
  };

  self.setBannerOffset = function () {
    var $subNav = $(".sub-nav");
    self.bannerOffset = 0;
    if (!Modernizr.touch && $subNav.length) {
      self.bannerOffset = $subNav.outerHeight() - 1;
    }
  };

  self.scrollTo = function (e) {
    e.preventDefault();
    self.scrollToTarget($(e.currentTarget).attr("href"));
  };

  self.scrollToTarget = function (targetSelector) {
    var $targetElem,
        scrollAmount;
    $targetElem = $(targetSelector);
    if ($targetElem.length) {
      scrollAmount = $targetElem.offset().top - self.bannerOffset;

      $("html, body").animate({
        scrollTop: scrollAmount
      }, 400);
    }
  };

  return {
    initialize: function () {
      self.setBannerOffset();
      self.enableBindings();
    },
    onResize: function (scrollCallback) {
      self.callbacks.push(scrollCallback);
    },
  };
});
