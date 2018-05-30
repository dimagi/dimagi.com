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
  'careers/list',
], function (
  $,
  _,
  List
) {
  'use strict';
  $(function () {
      List.initialize();
  });
});
