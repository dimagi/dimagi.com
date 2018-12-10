/* globals window */
define([
  'jquery',
  'lodash',
  'app/analytix/utils',
  'app/analytix/logging',
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

   /**
   * Tracks a click through the Hubspot API
   * @param {(object|string)} element - The element (or a selector) whose clicks you want to track.
   * @param {string} eventId - The ID of the event. If you created the event in HubSpot, use the numerical ID of the event.
   * @param {integer|float} value - This is an optional argument that can be used to track the revenue of an event.
   */
  var trackClick = function (
      element,
      eventId,
      value
  ) {
    self.ready.done(function () {
      Utils.trackClickHelper(
          element,
          function (callbackFn) {
            trackEvent(eventId, value);
          }
      );
      self.logger.debug.log(self.logger.fmt.labelArgs([
        "Element",
        "EventId",
        "Value"
      ], arguments), "Added Click Tracker");

    });
  };


  var bindEvents = function () {

    _.each($('[data-hsq="true"]'), function ($elem) {

      $elem = $($elem);

      var eventId = $elem.attr('data-hsq-id'),
          value = $elem.attr('data-hsq-value');

      trackClick($elem, eventId, value);

    });

  };

  var onFormsReadyCallback = function (callback) {
    self.onFormsReady.done(callback);
  };


  return {
    initialize: function () {
      $(function () {
        var apiId = Utils.getApiId('HUBSPOT'),
            scriptUrl = '//js.hs-scripts.com/' + apiId + '.js';

        self.logger = Logging.getLoggerForApi('Hubspot');

        self.ready = $.Deferred();
        self.onFormsReady = $.Deferred();
        self.ready = Utils.initApi(self.ready, apiId, scriptUrl, self.logger, function () {
          bindEvents();
        });

        self.ready.done(function () {
            var formScriptUrls = ['//js.hsforms.net/forms/v2.js'];
            if ($('html').hasClass('lt-ie9')) {
                formScriptUrls = _.union(['//js.hsforms.net/forms/v2-legacy.js'], formScriptUrls);
            }

            $.when.apply($, _.map(formScriptUrls, function (url) { return $.getScript(url); }))
              .done(function () {
                  self.onFormsReady.resolve();
              });
          });
      });
    },
    apiId: function () {
      return Utils.getApiId('HUBSPOT');
    },
    identify: identify,
    trackEvent: trackEvent,
    onFormsReady: onFormsReadyCallback,
  };
});
