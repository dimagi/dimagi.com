define([
  'lodash',
  'app/analytix/utils',
  'app/analytix/hubspot',
  'app/analytix/kissmetrix',
  'app/analytix/drift',
  'app/analytix/wistia',
], function (
    _,
    Utils,
    Hubspot,
    Kissmetrics,
    Drift,
    Wistia
) {
  'use strict';
  var self = {};
  self.trackingModules = [
      Utils,
      Hubspot,
      Kissmetrics,
      Drift,
      Wistia
  ];

  return {
    initialize: function () {
      _.each(self.trackingModules, function (mod) {
        mod.initialize();
      });
    },
  };
});
