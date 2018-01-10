define([
  'lodash',
  'jquery',
], function (_, $) {
  'use strict';
  var self = {};
  self.callbacks = [];

  self.enableBindings = function () {
    $(window).on("resize", function() {
      if (self.delayResize && clearTimeout(self.delayResize)) {
        self.delayResize = setTimeout(function () {
          self.recalcLayout();
        }, 100);
      }
    });
  };

  self.recalcLayout = function () {
    _.each(self.callbacks, function (fn) {
      if (_.isFunction(fn)) {
        fn.call();
      }
    });
  };

  return {
    initialize: function () {
      self.enableBindings();
    },
    onResize: function (scrollCallback) {
      self.callbacks.push(scrollCallback);
    },
  };
});
