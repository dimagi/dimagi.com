/* global Array, window */

/**
 * Instantiates the Drift analytics and customer support messaging platform.
 */

define([
  'jquery',
  'lodash',
  'app/analytix/utils',
  'app/analytix/logging',
  'app/analytix/hubspot',
], function (
    $,
    _,
    Utils,
    Logging,
    Hubspot
) {
  'use strict';
  var self = {},
      _drift = {};
  return {
    initialize: function () {
      self.hideDrift = $("meta[property='dimagi:driftHide']").attr("content");
      if (self.hideDrift) return;

      var apiId = Utils.getApiId('DRIFT'),
          scriptUrl = "https://js.driftt.com/include/" + Utils.getDateHash() + "/" + apiId + '.js';

      self.logger = Logging.getLoggerForApi('Drift');
      self.ready = $.Deferred();
      self.ready = Utils.initApi(self.ready, apiId, scriptUrl, self.logger, function() {
        _drift = window.driftt = window.drift = window.driftt || [];
        if (!_drift.init && !_drift.invoked ) {
          _drift.methods = [
            "identify",
            "config",
            "track",
            "reset",
            "debug",
            "show",
            "ping",
            "page",
            "hide",
            "off",
            "on"
          ];
          _drift.factory = function (methodName) {
            return function() {
              var methodFn = Array.prototype.slice.call(arguments);
              methodFn.unshift(methodName);
              _drift.push(methodFn);
              return _drift;
            };
          };
          _.each(_drift.methods, function (methodName) {
            _drift[methodName] = _drift.factory(methodName);
          });
        }

        _drift.SNIPPET_VERSION = '0.3.1';

        _drift.on('emailCapture',function(e){
          Hubspot.identify({email: e.data.email});
          Hubspot.trackEvent('Identified via Drift');
        });

        $('a[href="#demo-request"]').click(function () {
          console.log('start demo drift');
          _drift.api.startInteraction({ interactionId: 43079 });
        });
      });

    },
  };
});
