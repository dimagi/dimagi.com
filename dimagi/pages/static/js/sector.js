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
  'sector/select_sector',
  'sector/sub_sector'
], function (
  $,
  _,
  select_sector,
  sub_sector
) {
  'use strict';
  $(function () {
    select_sector.initialize();
    sub_sector.initialize();
  });
});
