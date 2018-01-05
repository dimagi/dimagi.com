require([
  'jquery',
  'lodash',
  'app/menu',
  'app/showTime',
  'app/modal',
], function ($, _, menu, showTime, modal) {
  $(function () {
    _.each([
      menu,
      showTime,
      modal,
    ], function (m) {
      m.initialize();
    });
  });

});
