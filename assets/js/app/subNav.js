define([
  'jquery',
  'modernizr',
  'app/constants',
  'app/pipeline',
  'app/resize',
], function (
    $,
    Modernizr,
    Constants,
    Pipeline,
    Resize
) {
  'use strict';
  var self = {};

  self.CLASSES = {
    SUB_NAV: "sub-nav",
    FIXED: "sub-nav-fixed",
    FIXED_TOP: "sub-nav-fixed-top",
    FIXED_BOTTOM: "sub-nav-fixed-bottom",
    MENU_ACTIVE: "sub-nav-menu-active",
  };

  self.enableMenu = function () {
    $(document).on("click.subNavOpen", ".prompt-link", function(e) {
      return e.preventDefault(), self.toggleMenu();
    });
    $(document).on("click.subNavOpen", ".dropdown-toggle", function(e) {
      return e.preventDefault(), self.toggleMenu();
    });
  };

  self.toggleMenu = function () {
    self.menuActive ? self.deactivateMenu() : self.activateMenu();
  };

  self.activateMenu = function () {
    self.$html.addClass(self.CLASSES.MENU_ACTIVE);
    self.menuActive = true;
    $(document)
      .on("click.subNavClose", function (e) {
        var n = $(e.target);
        if (n.closest(".sub-nav").length === 0 ||
            (n.is("a") && (n.parents(".destinations").length || n.parents(".dropdown").length))) {
          self.deactivateMenu();
        }
      })
      .on("keydown.subNavClose", function(e) {
        if (self.menuActive && e.keyCode === Constants.ESC_KEY_CODE) {
          self.deactivateMenu();
        }
      });
  };

  self.deactivateMenu = function () {
    $(document).off(".subNavClose");
    self.$html.removeClass(self.CLASSES.MENU_ACTIVE);
    self.menuActive = false;
  };

  self.enableFixedNav = function () {
    var $fixedNav;
    self.offsetTop = self.$subNav.offset().top;
    $fixedNav = self.$subNav.clone();
    $fixedNav.addClass(self.CLASSES.FIXED);
    self.$subNav.after($fixedNav);

    Pipeline.onScroll(function () {
      self.updateFixedNav();
    });

    Resize.onResize(function () {
      self.offsetTop = self.$subNav.offset().top;
      self.updateFixedNav();
    });

  };

  self.updateFixedNav = function () {
    if (self.fixedToTop && Pipeline.getScrollPosition() < self.offsetTop) {
      self.deactivateFixedNav();
    } else if (Pipeline.getScrollPosition() >= self.offsetTop) {
      self.activateFixedNav();
    }
  };

  self.activateFixedNav = function () {
    self.$html.addClass(self.CLASSES.FIXED_TOP);
    self.fixedToTop = true;
  };

  self.deactivateFixedNav = function () {
    self.$html.removeClass(self.CLASSES.FIXED_TOP);
    self.fixedToTop = false;
  };

  return {
    initialize: function () {
      var subNavs = $("." + self.CLASSES.SUB_NAV);
      if (subNavs.length) {
        self.menuActive = false;
        self.fixedToTop = false;
        self.fixedTopBottom = false;
        self.$html = $("html");

        self.$subNav = subNavs.first();
        self.enableMenu();

        if (Modernizr.touch) {
          self.$html.addClass(self.CLASSES.FIXED_BOTTOM);
          self.fixedToBottom = true;
        } else {
          self.enableFixedNav();
        }
      }
    }
  };
});
