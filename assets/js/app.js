requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min"
  }
});

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

    var ua = navigator.userAgent,
    iOS = /iPad|iPhone|iPod/.test(ua),
    iOS11 = /OS 11_0|OS 11_1|OS 11_2/.test(ua);

    // ios 11 bug caret position
    if ( iOS && iOS11 ) {
      // Add CSS class to body
      $("html").addClass("ios-modal-fix");
    }

  });
});
