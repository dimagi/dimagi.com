requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min"
  }
});

require([
  'jquery',
  'lodash',
  'app/subNav',
  'app/amp',
  'app/progressBar',
  'app/imageLoader',
  'app/transition',
  'app/extensions',
  'app/modal',
  'app/analytix',
  'app/demoForm',
  'app/initial',
  'modernizr',
], function (
    $,
    _,
    SubNav,
    AMP,
    ProgressBar,
    ImageLoader,
    Transition,
    Extensions,
    Modal,
    Analytix,
    DemoForm,
    Initial
) {
  $(function () {
    _.each([
      SubNav,
      AMP,
      ProgressBar,
      ImageLoader,
      Extensions,
      Transition,
      Modal,
      Analytix,
      DemoForm,
      Initial,
    ], function (m) {
      m.initialize();
    });
  });
});
