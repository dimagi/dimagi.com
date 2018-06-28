define([
  'lodash',
  'jquery',
], function (
  _,
  $
) {
  'use strict';

  var module = {};

  module.hideAllCards = function () {
    $('.quick-start-intro-main').fadeOut(0);
    $('.quick-start-card').fadeOut(0);
    $('.quick-start-header').fadeOut(0);
  };

  module.showCardTheme = function (cardTheme) {
    $('.quick-start-card-'+cardTheme).fadeIn();
    $('.quick-start-header-'+cardTheme).fadeIn();
  };

  module.enableBindings = function () {

    $(document).click(function (e) {
      if (!$(e.target).closest(".selected-card").length) {
        $(".card-selector").removeClass("show");
      }
    });

    $('.selected-card').click(function (e) {
      e.preventDefault();
      $('.card-selector').addClass('show');
    });

    $('.card-selector li').click(function (e) {
      var cardTheme = $(this).data('theme');
      module.hideAllCards();
      module.showCardTheme(cardTheme);
    });
  };

  return {
    initialize: function () {
      module.enableBindings();
      $('.selected-container').fadeIn();
    },
  };
});

