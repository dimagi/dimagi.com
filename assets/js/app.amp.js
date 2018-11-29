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
    'app/progressBar',
    'app/imageLoader',
    'app/pipeline',
    'app/resize',
    'modernizr',
  ], function (
      $,
      _,
      ProgressBar,
      ImageLoader,
      SubNav,
      Pipeline ,
      Resize,
  ) {
    $(function () {
      _.each([
        ProgressBar,
        ImageLoader,
        SubNav, 
        Pipeline ,
        Resize,
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
  