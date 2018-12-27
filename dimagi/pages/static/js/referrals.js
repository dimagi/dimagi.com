requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min",
    knockout: "lib/knockout/knockout-latest"
  }
});

require([
  'jquery',
  'lodash',
  'quick_start/selector',
], function (
  $,
  _,
  Selector
) {
  'use strict';
  $(function () {
      Selector.initialize();
  });
});
