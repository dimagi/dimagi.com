/* global window, Wistia */

define([
  'jquery',
], function (
    $
) {
  'use strict';

  return {
    initialize: function () {
      var videoId = $("meta[property='wistia:videoId']").attr('content'),
          videoTrigger =  $("meta[property='wistia:videoTrigger']").attr('content');

      if (videoId && videoTrigger) {
        window._wq = window._wq || [];
        window._wq.push({id: videoId, onReady: function (video) {
          if (window.location.href.indexOf('#' + videoTrigger) !== -1) {
            video.popover.show();
          }
        }});
      }

    },
  };
});
