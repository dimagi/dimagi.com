define([
    'lodash',
    'app/tracking/utils',
    'app/tracking/google',
    'app/tracking/hubspot',
    'app/tracking/kissmetrix',
    'app/tracking/drift',
], function (
    _,
    Utils,
    Google,
    Hubspot,
    Kissmetrics,
    Drift
) {
  'use strict';
  var self = {};
  self.trackingModules = [
      Utils,
      Google,
      Hubspot,
      Kissmetrics,
      Drift
  ];

  return {
    initialize: function () {
      _.each(self.trackingModules, function (mod) {
        mod.initialize();
      });
    },
  };
});
