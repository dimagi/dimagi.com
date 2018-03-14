require([
  'jquery',
  'lodash',
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
  'modernizr',
], function (
    $,
    _,
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
    Transition
) {
  $(function () {
    _.each([
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
    ], function (m) {
      m.initialize();
    });
  });
});
