define([
  'jquery',
], function (
  $
) {
  'use strict';
  var self = {};
  self.isAmp = false;
  self.pageType = 'unknown';

  return {
    initialize: function () {
      self.isAmp = $.parseJSON($("meta[property='dimagi:isAmp']").attr("content"));
      self.pageType = $("meta[property='dimagi:ampPageType']").attr("content");
    },
    enabled: function () {
      return self.isAmp;
    },
    pageType: function () {
      return self.pageType;
    },
  };
});
