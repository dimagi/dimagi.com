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
  // 'app/extensions',
  'modernizr',
], function (
    $,
    _,
    SubNav,
    AMP,
    ProgressBar,
    ImageLoader,
    Initial,
    Transition
    // Extensions
) {
  $(function () {
    _.each([
      SubNav,
      AMP,
      ProgressBar,
      ImageLoader,
      // Extensions,
      Transition,
      Initial,
    ], function (m) {
      m.initialize();
    });
  });
});
