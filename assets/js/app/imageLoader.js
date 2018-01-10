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
    self.$images = $('.image-loader[data-loading="true"] img');
    self.$lazyImages = self.$images.filter("[data-src]");
  };

  self.bindEvents = function () {
    self.$images.one("load", function(e) {
      self.onImageLoad(e.target);
    });
    _.each(self.$images, function (img) {
      if (img.complete && !$(img).attr("data-src")) {
        self.onImageLoad(img);
      }
    });
    if (self.$lazyImages.length) {
      Pipeline.onScroll(function () {
        self.lazyCheck();
      });
      Resize.onResize(function () {
        self.lazyCheck();
      });
      self.$document.on(Constants.EVENTS.CAROUSEL_REPAINT, function () {
        self.lazyCheck();
      });
    }
  };

  self.onImageLoad = function (img) {
    $(img).closest(".image-loader[data-loading]").attr("data-loading", false);
  };

  self.lazyCheck = function () {
    if (self.$lazyImages) {
      _.each(self.$lazyImages.filter("[data-src]"), function (img) {
        var loader = $(img).closest(".image-loader[data-loading]").get(0);
        if (self.isVisible(loader) && self.inView(loader)) {
          self.loadImage(img);
        }
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
  };

  return {
    initialize: function () {
      self.getHtml();
      self.bindEvents();
      self.lazyCheck();
    }
  };
});
