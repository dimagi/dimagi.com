define([
  'jquery',
  'lodash',
], function (
    $,
    _
) {
  'use strict';
  var self = {};

  self.SELECTORS = {
    MOBILE: '.js-partners-mobile',
    WEB: '.js-partners-web',
  };

  self.mode = 'web';

  self.columns = {
    web: [],
    mobile: [],
  };

  function Column(elem) {
    var col = this;
    col.elem = elem;
    col.logos = $(elem).find('.partner-logo');

    col.change = function () {
      var newLogo = _.random(0, col.logos.length - 1);
      if (newLogo === $(elem).find('.partner-logo.current').index()) {
        col.change();
      } else {
        $(elem).find('.partner-logo.current').fadeOut(400, function () {
          $(this).removeClass('current');
          $(col.logos[newLogo]).fadeIn(400, function () {
            $(elem).find('.partner-logo.current').removeClass('current');
            $(this).addClass('current');
          });
        });
      }
    };
  }

  function updateMode() {
    if (window.outerWidth < 718 ) {
      self.mode = 'mobile';
    } else {
      self.mode = 'web';
    }
  }

  return {
    initialize: function () {
      _.each($(self.SELECTORS.WEB + ' .column'), function (elem) {
        self.columns.web.push(new Column(elem));
      });
      _.each($(self.SELECTORS.MOBILE + ' .column'), function (elem) {
        self.columns.mobile.push(new Column(elem));
      });

      setInterval(function () {
        updateMode();

        var col = _.random(0, self.columns[self.mode].length - 1);
        self.columns[self.mode][col].change();

      }, 3000);
    },
  };
});
