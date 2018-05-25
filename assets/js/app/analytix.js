define([
  'lodash',
  'app/analytix/utils',
  'app/analytix/google',
  'app/analytix/hubspot',
  'app/analytix/kissmetrix',
  'app/analytix/drift',
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
