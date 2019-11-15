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
  'app/initial',
  'app/menu',
  'app/showTime',
  'app/pipeline',
  'app/subNav',
  'app/smoothScroll',
  'app/carousel',
  'app/imageLoader',
  'app/partners',
  'app/accordion',
  'app/transition',
  'app/resize',
  'app/modal',
  'app/analytix',
  'app/contactForm',
  'app/demoForm',
  'app/subscriptionForm',
  'app/topBannerAd',
  'app/abAudit',
  'app/progressBar',
  'modernizr',
], function (
    $,
    _,
    AMP,
    Initial,
    Menu,
    ShowTime,
    Pipeline,
    SubNav,
    SmoothScroll,
    Carousel,
    ImageLoader,
    Partners,
    Accordion,
    Transition,
    Resize,
    Modal,
    Analytix,
    ContactForm,
    DemoForm,
    SubscriptionForm,
    TopBannerAd,
    ABAudit,
    ProgressBar
) {
  $(function () {
    _.each([
      AMP,
      Initial,
      Menu,
      ShowTime,
      Pipeline,
      SubNav,
      SmoothScroll,
      Carousel,
      ImageLoader,
      Partners,
      Accordion,
      Transition,
      Resize,
      Modal,
      Analytix,
      ContactForm,
      DemoForm,
      SubscriptionForm,
      TopBannerAd,
      ABAudit,
      ProgressBar,
    ], function (m) {
      m.initialize();
    });
  });
});
