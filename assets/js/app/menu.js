define([
  'jquery',
], function (
    $
) {
  'use strict';
  var self = {};

  self.activate = function () {
    self.$html.addClass("menu-active");
  };

  self.deactivate = function () {
    self.$html.removeClass("menu-active");
  };

  self.enableBindings = function () {
    $(document).on("click.navMenuClose", ".menu-close", function (e) {
      e.preventDefault();
      self.deactivate();
    });
    $(document).on("click.navMenuOpen", ".menu-open", function (e) {
      e.preventDefault();
      self.activate();
    });
    $(document).on("keydown.navMenuClose", function (e) {
      if (e.keyCode === 27) self.deactivate();
    });
    $(document).on("click.navMenuClose", function (e) {
      if ($(e.target).closest(".menu, .banner").length === 0) {
        self.deactivate();
      }
    });
  };

  return {
    initialize: function () {
      self.$html = $("html");
      self.enableBindings();
    }
  };
});
