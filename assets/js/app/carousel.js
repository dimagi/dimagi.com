define([
  'jquery',
  'lodash',
  'modernizr',
  'app/resize',
  'app/constants',
], function (
    $,
    _,
    Modernizr,
    Resize,
    Constants
) {
  'use strict';
  var self = {};
  self.carousels = [];
  self.EVENTS = {
    ORIENTATION_CHANGE: "orientationchange.app.carousel",
    CLICK: "click.app.carousel",
    TOUCH_START: "touchstart.app.carousel",
    TOUCH_MOVE: "touchmove.app.carousel",
    TOUCH_END: "touchend.app.carousel",
    MOUSE_DOWN: "mousedown.app.carousel",
    MOUSE_MOVE: "mousemove.app.carousel",
    MOUSE_UP: "mouseup.app.carousel",
    TRANSITION_END: "transitionend webkitTransitionEnd",
  };
  self.ATTR = {
    LOADING: "data-loading",
    DOT: "data-dot",
    ACTIVE: "data-active",
    ANIMATING: "data-animating",
    DRAGGING: "data-dragging",
  };
  self.SELECTORS = {
    CAROUSEL: ".carousel",
    SLIDE: ".carousel-slide",
    SLIDER: ".carousel-slider",
    CONTAINER: ".carousel-container",
    ARROW: ".carousel-arrow",
    DOT: "[" + self.ATTR.DOT + "]",
  };

  self.get = function (index) {
    var matches;

    if (_.isInteger(index) && index < self.carousels.length) {
      return self.carousels[index];
    }

    matches = _.filter(self.carousels, function (c) {
      return c.id === index;
    });

    return matches.carousels.length ? matches.carousels[0] : null;
  };

  var Carousel = function (selector) {
    var model = this;
    model.FLING_TIMEOUT = 500;

    model.initialize = function () {
      model.$carousel = $(selector);
      model.$carousel.attr(self.ATTR.LOADING, true);
      model.getHtml();
      model.getData();
      model.bindEvents();
      if (model.hasDots && !model.hideDots) {
        model.buildDots();
      }
      if (model.hasArrows) {
        model.buildArrows();
      }
      model.onResize();
      model.updateUI();
      model.$carousel.attr(self.ATTR.LOADING, false);
    };

    model.getHtml = function () {
      model.$window = $(window);
      model.$container = model.$carousel.find(self.SELECTORS.CONTAINER);
      model.$slider = model.$container.find(self.SELECTORS.SLIDER);
      model.$slides = model.$slider.find(self.SELECTORS.SLIDE);
    };

    model.getData = function () {
      model.id = model.$carousel.attr("id");
      model.isTouch = Modernizr.touch;
      model.index = 1;
      model.count = model.$slides.length;
      model.position = 0;
      model.hasDots = model.count > 1;
      model.hideDots = model.$carousel.hasClass('hide-dots');
      model.hasArrows = model.$carousel.hasClass('carousel-arrows');
    };

    model.bindEvents = function () {
      Resize.onResize(function () {
        model.onResize();
      });
      model.$window.on(self.EVENTS.ORIENTATION_CHANGE, function () {
        model.onResize();
      });
      model.$carousel.on(self.EVENTS.CLICK, self.SELECTORS.SLIDE, function (e) {
        model.onSlideClick(e);
      });
      if (model.hasDots) {
        model.$carousel.on(self.EVENTS.CLICK, self.SELECTORS.DOT, function (e) {
          model.onDotClick(e);
        });
      }
      if (model.hasArrows) {
        model.$carousel.on(self.EVENTS.CLICK, self.SELECTORS.ARROW, function (e) {
          // re-using functionality from dots for arrows
          model.onDotClick(e);
        });
      }
      if (model.isTouch) {
        model.$carousel.on(self.EVENTS.TOUCH_START, function (e) {
          model.onDragStart(e);
        });
        model.$container.on(self.EVENTS.TOUCH_MOVE, function (e) {
          model.onDragUpdate(e);
        });
        model.$container.on(self.EVENTS.TOUCH_END, function (e) {
          model.onDragEnd(e);
        });
      } else {
        model.$container.on(self.EVENTS.MOUSE_DOWN, function (e) {
          model.onDragStart(e);
        });
      }
    };

    model.onResize = function () {
      model.carouselWidth = model.$container.innerWidth();
      model.carouselCenter = Math.round(model.carouselWidth / 2);
      model.goToSlide(model.index);
    };

    model.onSlideClick = function (e) {
      var target = $(e.currentTarget);
      if (target.attr(self.ATTR.ACTIVE) !== "true") {
        e.preventDefault();
        model.goToSlide(target.index() + 1);
      }
    };

    model.onDotClick = function (e) {
      var target = $(e.currentTarget),
          ind = target.attr(self.ATTR.DOT);
      e.preventDefault();
      if (model.index !== ind) {
        if (!model.hideDots) {
          model.$dots.find(self.SELECTORS.DOT).attr(self.ATTR.ACTIVE, false);
          target.attr(self.ATTR.ACTIVE, true);
        }
        model.goToSlide(ind);
      }
    };

    model.onDragStart = function (e) {
      if (model.isTouch || e.button === 0) {
        if (model.$slider.attr(self.ATTR.ANIMATING) === "true") model.freezeAnimation();
        model.$slider.attr(self.ATTR.DRAGGING, true);
        model.startFlingTimeout();
        if (!model.isTouch) {
          model.$window.on(self.EVENTS.MOUSE_MOVE, function(e) {
            model.onDragUpdate(e);
          });
          model.$window.on(self.EVENTS.MOUSE_UP, function(e) {
            model.onDragEnd(e);
          });
        }
        model.calculateDrag(e);
      }
    };

    model.onDragUpdate = function (e) {
      model.calculateDrag(e);
      if (model.dragNow.isDrag || !model.isTouch) {
        e.preventDefault();
        model.goToPosition(model.dragNow.position);
      }
    };

    model.onDragEnd = function(e) {
      var ind;
      if (!model.isTouch) {
        model.$window.off(self.EVENTS.MOUSE_MOVE);
        model.$window.off(self.EVENTS.MOUSE_UP);
      }
      if (model.dragNow.directionX !== 0) {
        model.$carousel.one(self.EVENTS.CLICK, function (e) {
          e.preventDefault();
          e.stopPropagation();
        });
      }
      model.$slider.attr(self.ATTR.DRAGGING, false);
      ind = model.index;
      if (model.dragNow.isDrag || !model.isTouch) {
        e.preventDefault();
      }
      if (model.isFling) {
        ind += model.dragNow.directionX;
      } else {
        ind = model.indexFromPosition(model.position);
      }
      model.goToSlide(ind);
      model.dragStart = model.dragNow = undefined;
    };

    model.calculateDrag = function (e) {
      var startDragging,
          position,
          eventX,
          eventY,
          directionX,
          isDrag,
          curMove,
          movedX,
          movedY,
          absX,
          absY;
      startDragging = !(model.dragStart && model.dragNow);

      if (e.touches && e.touches[0]) {
        eventX = e.touches[0].clientX;
        eventY = e.touches[0].clientY;
      } else {
        eventX = e.clientX;
        eventY = e.clientY;
      }

      if (startDragging) {
        position = model.position;
        directionX = 0;
        isDrag = null;
      } else {
        curMove = model.dragNow.eventX - eventX;
        position = model.dragNow.position + curMove;
        movedX = model.dragStart.eventX - eventX;
        movedY = model.dragStart.eventY - eventY;
        absX = Math.abs(movedX);
        absY = Math.abs(movedY);
        directionX = (function() {
          if (movedX > 0) return 1;
          if (movedX < 0) return -1;
          return 0;
        }());
        isDrag = null === model.dragNow.isDrag ? absX > absY : model.dragNow.isDrag;
      }
      model.dragNow = {
        eventX: eventX,
        eventY: eventY,
        position: position,
        isDrag: isDrag,
        directionX: directionX,
      };
      if (startDragging) {
        model.dragStart = _.create(model.dragNow);
      }
    };

    model.startFlingTimeout = function () {
      model.isFling = true;
      setTimeout(function () {
        model.isFling = false;
      }, model.FLING_TIMEOUT);
    };

    model.goToSlide = function (ind) {
      var curPos;
      model.setIndex(ind);
      curPos = model.positionFromIndex(model.index);
      if (model.position !== curPos) {
        model.$slider.attr(self.ATTR.ANIMATING, "true");
        model.$slider.one(self.EVENTS.TRANSITION_END, function (e) {
          model.$slider.attr(self.ATTR.ANIMATING, "false");
          model.$carousel.trigger(Constants.EVENTS.CAROUSEL_REPAINT);
        });
        model.goToPosition(curPos);
      }
    };

    model.setIndex = function (ind) {
      ind = Math.min(Math.max(ind, 1), model.count);
      if (model.index !== ind) {
        model.index = ind;
        model.updateUI();
      }
    };

    model.goToPosition = function (pos) {
      model.position = pos;
      requestAnimationFrame(function () {
        model.$slider.css({
          transform: "translateX(" + -pos + "px)",
        });
        model.$carousel.trigger(Constants.EVENTS.CAROUSEL_REPAINT);
      });
    };

    model.positionFromIndex = function (ind) {
      var elem, delta;
      elem = model.$slides.eq(ind - 1);
      delta = elem.position().left + elem.innerWidth() / 2;
      return delta - model.carouselCenter;
    };

    model.indexFromPosition = function (pos) {
      var finalIndex,
          curPos,
          finPos,
          delta,
          ind,
          a,
          r;
      finalIndex = 1;
      finPos = Number.POSITIVE_INFINITY;
      for (ind = r = 1, a = model.count;
           a >= 1 ? a >= r : r >= a;
           ind = a >= 1 ? ++r : --r) {
        curPos = model.positionFromIndex(ind);
        delta = Math.abs(pos - curPos);
        if (delta < finPos) {
          finPos = delta;
          finalIndex = ind;
        }
      }
      return finalIndex;
    };

    model.freezeAnimation = function () {
      var transformStyle, transformAmt;
      model.$slider.off(self.EVENTS.TRANSITION_END);
      transformStyle = getComputedStyle(model.$slider[0]).transform;
      transformAmt = parseInt(transformStyle.split(",")[4].trim());
      model.goToPosition(-transformAmt);
      model.$slider.attr(self.ATTR.ANIMATING, "false");
    };

    model.buildDots = function () {
      var e, t, n;
      if (model.count > 1) {
        model.$dots = $('<nav class="carousel-dots" />');
        for (e = t = 1, n = model.count;
             n >= 1 ? n >= t : t >= n;
             e = n >= 1 ? ++t : --t)  {
          model.$dots.append($('<span data-dot="' + e + '" />'));
        }
        model.$carousel.append(model.$dots);
      }
    };

    model.buildArrows = function () {

      $(model.$slides).each(function (ind, slide) {
        var $prev, $next;
        if (ind > 0) {
          $prev = $('<div class="carousel-arrow previous"><div class="arrow-nav"></div></div>');
          $prev.attr('data-dot', ind);
          $(slide).append($prev);
        }
        if (ind < model.count - 1) {
          $next = $('<div class="carousel-arrow next"><div class="arrow-nav"></div></div>');
          $next.attr('data-dot', ind + 2);
          $(slide).append($next);
        }
      });
    };

    model.updateUI = function () {
      requestAnimationFrame(function() {
        model.updateSlides();
        if (model.hasDots && !model.hideDots) {
          model.updateDots();
        }
      });
    };

    model.updateDots = function() {
      model.$dots.find(self.SELECTORS.DOT).attr(self.ATTR.ACTIVE, false);
      model.$dots.find('['+self.ATTR.DOT+'="' + model.index + '"]').attr(self.ATTR.ACTIVE, true);
    };

    model.updateSlides = function() {
      model.$slides.attr(self.ATTR.ACTIVE, false);
      model.$slides.eq(model.index - 1).attr(self.ATTR.ACTIVE, true);
    };

  };

  return {
    initialize: function () {
      _.each($(self.SELECTORS.CAROUSEL), function (elem) {
        var carousel = new Carousel(elem);
        carousel.initialize();
        self.carousels.push(carousel);
      });
    },
  };
});
