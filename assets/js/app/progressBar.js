define([
  'jquery',
], function (
    $
) {
  'use strict';
  var self = {};

  self.updateMaxProgress = function () {
    var windowHeight = $(window).height(),
        docHeight = $(document).height(),
        maxProgress = docHeight - windowHeight;
    $('.progress-bar').each(function (ind, e) {
      $(e).attr("max", maxProgress);
    });
  };

  self.updateProgress = function (amount) {
    $('.progress-bar').each(function (ind, e) {
      $(e).attr("value", amount);
    });
  };

  self.enableBindings = function () {
    $(window)
        .off("scroll.progress")
        .on("scroll.progress", function () {
          self.updateProgress($(window).scrollTop());
        })
        .on("resize.progress", function () {
          self.updateMaxProgress();
        });
  };

  return {
    initialize: function () {
      self.updateMaxProgress();
      self.updateProgress($(window).scrollTop());
      self.enableBindings();
    },
    disable: function () {
      $(window).off("scroll.progress resize.progress");
    },
  };
});
