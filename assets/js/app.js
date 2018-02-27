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
    Analytix
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
    ], function (m) {
      m.initialize();
    });
  });
});
