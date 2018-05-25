define([
  'jquery',
  'lodash',
], function (
  $,
  _
) {
  'use strict';
  var self = {};

  function initEasing() {
    $.easing.jswing = $.easing.swing, $.extend($.easing, {
        def: "easeOutQuad",
        swing: function(t, n, i, r, o) {
            return $.easing[$.easing.def](t, n, i, r, o)
        },
        easeInQuad: function(e, t, n, i, r) {
            return i * (t /= r) * t + n
        },
        easeOutQuad: function(e, t, n, i, r) {
            return -i * (t /= r) * (t - 2) + n
        },
        easeInOutQuad: function(e, t, n, i, r) {
            return 1 > (t /= r / 2) ? i / 2 * t * t + n : -i / 2 * (--t * (t - 2) - 1) + n
        },
        easeInCubic: function(e, t, n, i, r) {
            return i * (t /= r) * t * t + n
        },
        easeOutCubic: function(e, t, n, i, r) {
            return i * ((t = t / r - 1) * t * t + 1) + n
        },
        easeInOutCubic: function(e, t, n, i, r) {
            return 1 > (t /= r / 2) ? i / 2 * t * t * t + n : i / 2 * ((t -= 2) * t * t + 2) + n
        },
        easeInQuart: function(e, t, n, i, r) {
            return i * (t /= r) * t * t * t + n
        },
        easeOutQuart: function(e, t, n, i, r) {
            return -i * ((t = t / r - 1) * t * t * t - 1) + n
        },
        easeInOutQuart: function(e, t, n, i, r) {
            return 1 > (t /= r / 2) ? i / 2 * t * t * t * t + n : -i / 2 * ((t -= 2) * t * t * t - 2) + n
        },
        easeInQuint: function(e, t, n, i, r) {
            return i * (t /= r) * t * t * t * t + n
        },
        easeOutQuint: function(e, t, n, i, r) {
            return i * ((t = t / r - 1) * t * t * t * t + 1) + n
        },
        easeInOutQuint: function(e, t, n, i, r) {
            return 1 > (t /= r / 2) ? i / 2 * t * t * t * t * t + n : i / 2 * ((t -= 2) * t * t * t * t + 2) + n
        },
        easeInSine: function(e, t, n, i, r) {
            return -i * Math.cos(t / r * (Math.PI / 2)) + i + n
        },
        easeOutSine: function(e, t, n, i, r) {
            return i * Math.sin(t / r * (Math.PI / 2)) + n
        },
        easeInOutSine: function(e, t, n, i, r) {
            return -i / 2 * (Math.cos(Math.PI * t / r) - 1) + n
        },
        easeInExpo: function(e, t, n, i, r) {
            return 0 === t ? n : i * Math.pow(2, 10 * (t / r - 1)) + n
        },
        easeOutExpo: function(e, t, n, i, r) {
            return t === r ? n + i : i * (-Math.pow(2, -10 * t / r) + 1) + n
        },
        easeInOutExpo: function(e, t, n, i, r) {
            return 0 === t ? n : t === r ? n + i : 1 > (t /= r / 2) ? i / 2 * Math.pow(2, 10 * (t - 1)) + n : i / 2 * (-Math.pow(2, -10 * --t) + 2) + n
        },
        easeInCirc: function(e, t, n, i, r) {
            return -i * (Math.sqrt(1 - (t /= r) * t) - 1) + n
        },
        easeOutCirc: function(e, t, n, i, r) {
            return i * Math.sqrt(1 - (t = t / r - 1) * t) + n
        },
        easeInOutCirc: function(e, t, n, i, r) {
            return 1 > (t /= r / 2) ? -i / 2 * (Math.sqrt(1 - t * t) - 1) + n : i / 2 * (Math.sqrt(1 - (t -= 2) * t) + 1) + n
        },
        easeInElastic: function(e, t, n, i, r) {
            e = 1.70158;
            var o = 0,
                s = i;
            return 0 === t ? n : 1 === (t /= r) ? n + i : (o || (o = .3 * r), s < Math.abs(i) ? (s = i, e = o / 4) : e = o / (2 * Math.PI) * Math.asin(i / s), -(s * Math.pow(2, 10 * --t) * Math.sin(2 * (t * r - e) * Math.PI / o)) + n);
        },
        easeOutElastic: function(e, t, n, i, r) {
            e = 1.70158;
            var o = 0,
                s = i;
            return 0 === t ? n : 1 === (t /= r) ? n + i : (o || (o = .3 * r), s < Math.abs(i) ? (s = i, e = o / 4) : e = o / (2 * Math.PI) * Math.asin(i / s), s * Math.pow(2, -10 * t) * Math.sin(2 * (t * r - e) * Math.PI / o) + i + n);
        },
        easeInOutElastic: function(e, t, n, i, r) {
            e = 1.70158;
            var o = 0,
                s = i;
            return 0 === t ? n : 2 === (t /= r / 2) ? n + i : (o || (o = .3 * r * 1.5), s < Math.abs(i) ? (s = i, e = o / 4) : e = o / (2 * Math.PI) * Math.asin(i / s), 1 > t ? -.5 * s * Math.pow(2, 10 * --t) * Math.sin(2 * (t * r - e) * Math.PI / o) + n : s * Math.pow(2, -10 * --t) * Math.sin(2 * (t * r - e) * Math.PI / o) * .5 + i + n)
        },
        easeInBack: function(e, t, n, i, r, o) {
            return void 0 === o && (o = 1.70158), i * (t /= r) * t * ((o + 1) * t - o) + n
        },
        easeOutBack: function(e, t, n, i, r, o) {
            return void 0 === o && (o = 1.70158), i * ((t = t / r - 1) * t * ((o + 1) * t + o) + 1) + n
        },
        easeInOutBack: function(e, t, n, i, r, o) {
            return void 0 === o && (o = 1.70158), 1 > (t /= r / 2) ? i / 2 * t * t * (((o *= 1.525) + 1) * t - o) + n : i / 2 * ((t -= 2) * t * (((o *= 1.525) + 1) * t + o) + 2) + n
        },
        easeInBounce: function(t, n, i, r, o) {
            return r - $.easing.easeOutBounce(t, o - n, 0, r, o) + i
        },
        easeOutBounce: function(e, t, n, i, r) {
            return (t /= r) < 1 / 2.75 ? 7.5625 * i * t * t + n : 2 / 2.75 > t ? i * (7.5625 * (t -= 1.5 / 2.75) * t + .75) + n : 2.5 / 2.75 > t ? i * (7.5625 * (t -= 2.25 / 2.75) * t + .9375) + n : i * (7.5625 * (t -= 2.625 / 2.75) * t + .984375) + n
        },
        easeInOutBounce: function(t, n, i, r, o) {
            return o / 2 > n ? .5 * $.easing.easeInBounce(t, 2 * n, 0, r, o) + i : .5 * $.easing.easeOutBounce(t, 2 * n - o, 0, r, o) + .5 * r + i
        }
    });
  };

  return {
    initialize: function () {
      initEasing();
    }
  };
});
