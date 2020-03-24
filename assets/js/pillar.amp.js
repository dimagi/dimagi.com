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
  'app/carousel',
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
    Carousel,
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
      Transition,
      Carousel,
      Modal,
      Analytix,
      DemoForm,
      Initial,
    ], function (m) {
      m.initialize();
    });
  });
});
