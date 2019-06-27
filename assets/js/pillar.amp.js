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
  'app/initial',
  'app/transition',
  'app/analytix',
  'app/demoForm',
  'modernizr',
], function (
    $,
    _,
    SubNav,
    AMP,
    ProgressBar,
    ImageLoader,
    Initial,
    Transition,
    Analytix,
    DemoForm
) {
  $(function () {
    _.each([
      SubNav,
      AMP,
      ProgressBar,
      ImageLoader,
      Transition,
      Analytix,
      DemoForm,
      Initial,
    ], function (m) {
      m.initialize();
    });
  });
});
