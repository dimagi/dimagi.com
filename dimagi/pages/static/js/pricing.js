requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min",
    knockout: "lib/knockout/knockout-latest"
  }
});

require([
  'knockout',
  'jquery',
  'lodash',
  'pricing/models',
], function (
  ko,
  $,
  _,
  Models
) {
  'use strict';
  $(function () {
    var page = Models.createPricingPage();
    ko.applyBindings(page, $('#ko-pricing-control').get(0));
  });

});
