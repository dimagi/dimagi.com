define([
  'app/constants',
  'app/pipeline',
  'app/resize',
  'jquery',
], function (Constants, Pipeline, Resize, $) {
  'use strict';
  var self = {};

  self.getHtml = function () {
    self.$window = $(window);
    self.$document = $(document);

    self.$images = $('[data-lazyimg="true"]');
    self.$backgrounds = $('[data-lazybg="true"]');
    self.$placeholders = $('[data-lazyplaceholder="true"]');
  };

  self.bindEvents = function () {

    Pipeline.onScroll(function () {
      self.lazyCheck();
    });

    Resize.onResize(function () {
      self.lazyCheck();
    });

    self.$document.on(Constants.EVENTS.CAROUSEL_REPAINT, function () {
      self.lazyCheck();
    });

    self.$document.on(Constants.EVENTS.MODAL_SHOW, function () {
      self.lazyCheck();
    });

  };

  self.lazyCheck = function () {

    if (self.$images) {
      self.$images = self.$images.filter("[data-src]");
      _.each(self.$images, function (img) {
        if (self.isVisible(img) && self.inView(img)) {
          self.loadImage(img);
        }
      });
    }

    if (self.$placeholders) {
      self.$placeholders = self.$placeholders.filter("[data-src]");
      _.each(self.$placeholders, function (img) {
        if (self.isVisible(img) && self.inView(img)) {
          self.loadPlaceholder(img);
        }
      });
    }

    if (self.$backgrounds) {
      self.$backgrounds = self.$backgrounds.filter('[data-lazybg]');
      _.each(self.$backgrounds, function (bg) {
        if (self.isVisible(bg) && self.inView(bg)) {
          self.loadBackground(bg);
        }
      });
      self.$backgrounds = self.$backgrounds.filter('[data-lazybg]');
      _.each(self.$backgrounds, function (bg) {
        self.loadBackground(bg);
      });
    }

  };

  self.isVisible = function (img) {
    return $(img).is(":visible");
  };

  self.inView = function (img) {
    var inWidth,
        inHeight,
        boundingRect;
    boundingRect = img.getBoundingClientRect();
    inWidth = 0 <= boundingRect.right && boundingRect.left <= self.$window.width();
    inHeight = 0 <= boundingRect.bottom && boundingRect.top <= self.$window.height();
    return inWidth && inHeight;
  };

  self.loadImage = function (img) {
    var $img = $(img);
    $img.attr({
      src: $img.attr("data-src"),
      "data-src": null
    });
    $img.closest(".image-loader[data-loading]").attr("data-loading", false);
    $img.attr('data-lazyimg', false);
  };

  self.loadPlaceholder = function (bg) {
    var $bg = $(bg),
        src = $(bg).attr('data-src');
    $('<img />').attr('src', src).on('load', function () {
      $(this).remove();
      $bg.css('background-image', 'url("' + src + '")');
      $bg.attr('data-lazyplaceholder', "loaded");
    });
    $bg.attr({
      "data-src": null,
    });
  };

  self.loadBackground = function (bg) {
    var $bg = $(bg);
    $bg.addClass('loaded');
    $bg.attr({
      "data-lazybg": null,
    });
  };

  return {
    initialize: function () {
      self.getHtml();
      self.bindEvents();
      self.lazyCheck();
    }
  };
});
