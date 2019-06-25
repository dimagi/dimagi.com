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
  'app/contactForm',
  'app/scheduleDemoForm',
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
    ContactForm,
    ScheduleDemoForm
) {
  $(function () {
    _.each([
      SubNav,
      AMP,
      ProgressBar,
      ImageLoader,
      Transition,
      ContactForm,
      ScheduleDemoForm,
      Initial,
    ], function (m) {
      m.initialize();
    });
  });
});
