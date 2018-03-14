define([
  'jquery',
  'lodash',
], function (
    $,
    _
) {
  'use strict';
  var self = {};
  self.ANIMATION = {
    duration: 300,
    easing: "easeInOutQuart"
  };

  self.TYPES =  {
    collapse: {
      on: {
        height: 0
      },
      off: {
        height: "scrollHeight"
      }
    },
    fade: {
      on: {
        opacity: 0
      },
      off: {
        opacity: 1
      }
    }
  };

  self.enableBindings = function () {
    $(document).on("click.transitionable",  "[data-transition-target]",
        function(e) {
          e.preventDefault();
          var targetSelectors = $(e.currentTarget)
                  .attr("data-transition-target").split(" "), //r
              targets = []; //s

          _.each(targetSelectors, function (selector) {
            targets.push(self.toggle("#" + selector));
          });
          return targets;
        }
    );
  };

  self.disableBindings = function () {
    $(document).off("click.transitionable");
  };

  self.toggle = function(selector) {
    switch ($(selector).attr("data-transition-state")) {
      case "transitioning":
        return !1;
      case "on":
        return self.off(selector);
      case "off":
        return self.on(selector);
      default:
        return self.on(selector);
    }
  };

  self.on = function(selector) {
    self.animate(selector, { state: "on" } );
  };

  self.off = function(selector) {
    self.animate(selector, { state: "off" } );
  };

  // todo cleanup
  self.animate = function (e, t) {
    var n, i, r, o, s, a, u, c, l, d;
      if (null === t && (t = {}), n = $(e), i = n.attr("data-transition-state") || "off", "transitioning" === i) return !1;
      if (c = t.state || self.oppositeState(i) || "on", d = t.types || n.attr("data-transition-types") || "", a = t.props || {}, i === c) return !1;
      if ($.isEmptyObject(a))
          for (u = d.split(" "), r = 0, o = u.length; o > r; r++) l = u[r], $.extend(a, self.TYPES[l][c]);
      return self.convertKeywords(a, n), $.isEmptyObject(a) ? !1 : (s = {}, $.extend(s, self.ANIMATION, {
          start: function() {
              return n.attr("data-transition-state", "transitioning"), "off" === c ? n.removeClass(d) : void 0;
          },
          done: function() {
              return "on" === c && n.addClass(d), n.removeAttr("style"), n.attr("data-transition-state", c);
          }
      }), self.updateLinks(n, c), n.stop().animate(a, s));
  };
  
  self.updateLinks = function(e, t) {
    var n, i;
    return i = $(e).attr("id"), n = $("[data-transition-target='" + i + "']"), n.attr("data-transition-state", t);
  };

  self.convertKeywords = function(e, t) {
      var n;
      return n = $(t), "scrollHeight" === e.height ? e.height = n[0].scrollHeight : void 0;
  };

  self.oppositeState = function(e) {
    switch (e) {
      case "on":
        return "off";
      case "off":
        return "on";
      default:
        return void 0;
    }
  };

  return {
    initialize: function () {
      self.enableBindings();
    }
  };
});
