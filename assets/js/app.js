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
  'app/tracking',
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
    Tracking
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
      Tracking,
    ], function (m) {
      m.initialize();
    });
  });
});
