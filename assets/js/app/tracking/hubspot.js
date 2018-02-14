/* globals window */
define([
  'jquery',
  'lodash',
  'app/tracking/utils',
  'app/tracking/logging',
], function (
    $,
    _,
    Utils,
    Logging
) {
  'use strict';
  var self = {},
      _hsq = window._hsq = window._hsq || [];


  /**
   * Sends data to Hubspot to identify the current session.
   * @param {object} data
   */
  var identify = function (data) {
    self.ready.done(function() {
      self.logger.debug.log(data, "Identify");
      _hsq.push(['identify', data]);
    });
  };


  /**
   * Tracks an event through the Hubspot API
   * @param {string} eventId - The ID of the event. If you created the event in HubSpot, use the numerical ID of the event.
   * @param {integer|float} value - This is an optional argument that can be used to track the revenue of an event.
   */
  var trackEvent = function (
      eventId,
      value
  ) {
    self.ready.done(function() {
      self.logger.debug.log(self.logger.fmt.labelArgs([
        "Event ID",
        "Value"
      ], arguments), 'Track Event');
      _hsq.push(['trackEvent', {
        id: eventId,
        value: value,
      }]);
    });
  };


  return {
    initialize: function () {
      $(function () {
        var apiId = Utils.getApiId('HUBSPOT'),
            scriptUrl = '//js.hs-scripts.com/' + apiId + '.js';

        self.logger = Logging.getLoggerForApi('Hubspot');

        self.ready = $.Deferred();
        self.ready = Utils.initApi(self.ready, apiId, scriptUrl, self.logger);
      });
    },
    identify: identify,
    trackEvent: trackEvent,
  };
});
