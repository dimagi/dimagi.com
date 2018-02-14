/* globals Array, window */
/**
 *  Handles communication with the google analytics API.
 */
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
  var self = {};

  var _gtag = function () {
    // This should never run, because all calls to _gtag should be
    // inside done handlers for ready, but just in case...
    self.logger.warning.log(arguments, 'skipped gtag');
  };

  /**
   * Helper function for sending a Google Analytics Event.
   *
   * @param {string} eventCategory - The event category
   * @param {string} eventAction - The event action
   * @param {string} eventLabel - (optional) The event label
   * @param {string} eventValue - (optional) The event value
   * @param {object} eventParameters - (optional) Extra event parameters
   * @param {function} eventCallback - (optional) Event callback fn
   */
  var trackEvent = function (
      eventCategory,
      eventAction,
      eventLabel,
      eventValue,
      eventParameters,
      eventCallback
  ) {
    self.ready.done(function () {
      var params = {
        event_category: eventCategory,
        event_label: eventLabel,
        event_value: eventValue,
        event_callback: eventCallback,
        event_action: eventAction,
      };
      if (_.isObject(eventParameters)) {
        params = _.extend(params, eventParameters);
      }
      self.logger.debug.log(self.logger.fmt.labelArgs([
        "Category",
        "Action",
        "Label",
        "Value",
        "Parameters",
        "Callback"
      ], arguments), "Event Recorded");
      _gtag('event', eventAction, params);
    }).fail(function () {
      if (_.isFunction(eventCallback)) {
        eventCallback();
      }
    });
  };


  /**
   * Tracks an event when the given element is clicked.
   * Uses a callback to ensure that the request to the analytics services
   * completes before the default click action happens. This is useful if
   * the link would otherwise navigate away from the page.
   * @param {(object|string)} element - The element (or a selector) whose clicks you want to track.
   * @param {string} eventCategory - The event category
   * @param {string} eventAction - The event action
   * @param {string} eventLabel - (optional) The event label
   * @param {string} eventValue - (optional) The event value
   * @param {object} eventParameters - (optional) Extra event parameters
   */
  var trackClick = function (
    element,
    eventCategory,
    eventAction,
    eventLabel,
    eventValue,
    eventParameters
  ) {
    self.ready.done(function () {
      Utils.trackClickHelper(
          element,
          function (callbackFn) {
            trackEvent(eventCategory, eventAction, eventLabel, eventValue, eventParameters, callbackFn);
          }
      );
      self.logger.debug.log(self.logger.fmt.labelArgs([
        "Element",
        "Category",
        "Action",
        "Label",
        "Value",
        "Parameters"
      ], arguments), "Added Click Tracker");
    });
  };


  /**
   * Helper function that pre-fills the eventCategory field for all the
   * tracking helper functions. Useful if you want to track a lot of items
   * in a particular area of the site.
   * e.g. "Report Builder" would be the category
   *
   * @param {string} eventCategory - The event category
   */
  var trackCategory = function (eventCategory) {
    return {
      /**
       * @param {string} eventAction - The event action
       * @param {string} eventLabel - (optional) The event label
       * @param {string} eventValue - (optional) The event value
       * @param {object} eventParameters - (optional) Extra event parameters
       * @param {function} eventCallback - (optional) Event callback fn
       */
      event: function (eventAction, eventLabel, eventValue, eventParameters, eventCallback) {
        trackEvent(eventCategory, eventAction, eventLabel, eventValue, eventParameters, eventCallback);
      },
      /**
       * @param {(object|string)} element - The element (or a selector) whose clicks you want to track.
       * @param {string} eventAction - The event action
       * @param {string} eventLabel - (optional) The event label
       * @param {string} eventValue - (optional) The event value
       * @param {object} eventParameters - (optional) Extra event parameters
       */
      click: function (element, eventAction, eventLabel, eventValue, eventParameters) {
        // directly reference what the module returns instead of the private function,
        // as some mocha tests will want to replace the module's returned functions
        trackClick(element, eventCategory, eventLabel, eventValue, eventParameters);
      },
    };
  };

  return {
    initialize: function () {
      var apiId = Utils.getApiId('GOOGLE'),
          scriptUrl = '//www.googletagmanager.com/gtag/js?id=' + apiId;

      self.logger = Logging.getLoggerForApi("Google Analytics");

      self.ready = $.Deferred();
      self.ready = Utils.initApi(self.ready, apiId, scriptUrl, self.logger, function () {
        window.dataLayer = window.dataLayer || [];
        _gtag = function () {
          window.dataLayer.push(arguments);
          self.logger.verbose.log(arguments, 'gtag');
        };
        _gtag('js', new Date());

        var user = {
          user_id: Utils.getConfig('userId') || 'none',
        };

        // Configure Gtag with User Info
        _gtag('config', apiId, user);
      });
    },
    track: {
      event: trackEvent,
      click: trackClick,
    },
    trackCategory: trackCategory,
  };
});
