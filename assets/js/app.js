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
    ImageLoader
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
    ], function (m) {
      m.initialize();
    });
  });
});
