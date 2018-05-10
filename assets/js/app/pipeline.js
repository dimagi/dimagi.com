define([
  'jquery',
  'lodash',
], function (
    $,
    _
) {
  'use strict';
  var self = {};
  self.callbacks = [];

  self.enableBindings = function () {
    $(window).on("scroll", function() {
      self.scrollEventHandler();
    });
  };

  self.updateScrollPosition = function() {
    self.scrollPosition = $(window).scrollTop();
  };

  self.scrollEventHandler = function () {
    self.updateScrollPosition();
    if (self.checkScrolling) {
      _.each(self.callbacks, function(callbackFn) {
        if (_.isFunction(callbackFn)) {
          callbackFn.call();
        }
      });
    }
  };

  self.checkPosition = function () {
    self.checkScrolling = true;
  };

  return {
    initialize: function () {
      self.scrollPosition = 0;
      self.checkScrolling = true;
      self.enableBindings();
      self.callbacks.push(self.checkPosition);
    },
    onScroll: function (fn) {
      self.callbacks.push(fn);
    },
    getScrollPosition: function () {
      return self.scrollPosition;
    },
  };
});
