requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min"
  }
});

require([
  'jquery',
  'lodash',
  'app/amp',
  'app/menu',
  'app/showTime',
  'app/modal',
  'app/pipeline',
  'app/resize',
  'app/subNav',
  'app/smoothScroll',
  'app/carousel',
  'app/imageLoader',
  'app/partners',
  'app/analytix',
  'app/accordion',
  'app/extensions',
  'app/transition',
  'app/contactForm',
  'app/demoForm',
  'app/abAudit',
  'app/progressBar',
  'app/initial',
  'modernizr',
], function (
    $,
    _,
    AMP,
    Menu,
    ShowTime,
    Modal,
    Pipeline,
    Resize,
    SubNav,
    SmoothScroll,
    Carousel,
    ImageLoader,
    Partners,
    Analytix,
    Accordion,
    Extensions,
    Transition,
    ContactForm,
    DemoForm,
    ABAudit,
    ProgressBar,
    Initial
) {
  $(function () {
    _.each([
      AMP,
      Menu,
      ShowTime,
      Modal,
      Pipeline,
      Resize,
      SubNav,
      SmoothScroll,
      Carousel,
      ImageLoader,
      Partners,
      Analytix,
      Accordion,
      Extensions,
      Transition,
      ContactForm,
      DemoForm,
      ABAudit,
      ProgressBar,
      Initial,
    ], function (m) {
      m.initialize();
    });
  });
});
