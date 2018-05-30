requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min"
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
