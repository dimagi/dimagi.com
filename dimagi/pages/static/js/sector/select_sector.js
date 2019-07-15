define([
  'lodash',
  'jquery',
], function (
  _,
  $
) {
  'use strict';

  var module = {};

  module.enableBindings = function () {

    $(document).click(function (e) {
      if (!$(e.target).closest('.selected-card').length) {
        $(".card-selector").removeClass("show");
      }
    });

    $('.words').click(function (e) {
      e.preventDefault();
      $('.card-selector').addClass('show');
    });

    $('.card-selector li').click(function (e) {
      $(".card-selector").removeClass("show");
    });

  };

  return {
    initialize: function () {
      module.enableBindings();
      $('.selected-container').fadeIn();
    },
  };
});
