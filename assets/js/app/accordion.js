define([
  'jquery',
  'lodash',
], function (
  $,
  _
) {
  'use strict';
  var self = {};

  self.enableBindings = function () {

    _.each($(".accordion"), function (elem) {
     var $accordion = $(elem);
     $accordion.find('.accordion-header').click(function () {
        if ($accordion.hasClass('collapsed')) {
           $accordion.removeClass('collapsed');
           $accordion.find('.accordion-content').slideDown();
        } else {
           $accordion.addClass('collapsed');
           $accordion.find('.accordion-content').slideUp();
        }
     });
    });

    _.each($(".accordion-group"), function (elem) {
      var $group = $(elem);

      $(document).on("click", "[data-accordion-group-expand='" + $group.attr('id') + "']", function (e) {
        e.preventDefault();
        _.each($group.find('.accordion'), function (elem) {
          var $accordion = $(elem);
          if ($accordion.hasClass('collapsed')) {
           $accordion.removeClass('collapsed');
           $accordion.find('.accordion-content').slideDown();
          }
        });
      });

      $(document).on("click", "[data-accordion-group-close='" + $group.attr('id') + "']", function (e) {
        e.preventDefault();
        _.each($group.find('.accordion'), function (elem) {
          var $accordion = $(elem);
          if (!$accordion.hasClass('collapsed')) {
           $accordion.addClass('collapsed');
           $accordion.find('.accordion-content').slideUp();
          }
        });
      });

    });
  };

  return {
    initialize: function () {
      self.enableBindings();
    }
  };
});
