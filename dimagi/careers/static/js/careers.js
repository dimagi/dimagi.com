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
