/* globals _kmq */

var _kmq = window._kmq = _kmq || [];

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
      _allAbTests = {};

  window.dataLayer = window.dataLayer || [];

  /**
   * Push data to _kmq by command type.
   * @param {string} commandName
   * @param {object} properties
   * @param {function|undefined} callbackFn - optional
   * @param {string|undefined} eventName - optional
   */
  var _kmqPushCommand = function (
      commandName,
      properties,
      callbackFn,
      eventName
  ) {
    self.ready.done(function() {
      var command, data;
      command = _.compact([commandName, eventName, properties, callbackFn]);
      _kmq.push(command);
      data = {
        event: 'km_' + commandName,
      };
      if (eventName) data.km_event = eventName;
      if (properties) data.km_property = properties;
      window.dataLayer.push(data);
      self.logger.verbose.log(command, [
        'window._kmq.push',
        'window.dataLayer.push',
        '_kmqPushCommand',
        commandName
      ]);
    }).fail(function() {
      callbackFn();
    });
  };

  /**
   * Identifies the current user
   * @param {string} identity - A unique ID to identify the session. Typically the user's email address.
   */
  var identify = function (identity) {
    self.ready.done(function() {
      self.logger.debug.log(arguments, 'Identify');
      _kmqPushCommand('identify', identity);
    });
  };

  /**
   * Sets traits for the current user
   * @param {object} traits - an object of traits
   * @param {function} callbackFn - (optional) callback function
   * @param {integer} timeout - (optional) timeout in milliseconds
   */
  var identifyTraits = function (traits, callbackFn, timeout) {
    self.ready.done(function() {
      self.logger.debug.log(self.logger.fmt.labelArgs(["Traits", "Callback Function", "Timeout"], arguments), 'Identify Traits (Set)');
      callbackFn = Utils.createSafeCallback(callbackFn, timeout);
      _kmqPushCommand('set', traits, callbackFn);
    }).fail(function() {
      if (_.isFunction(callbackFn)) {
        callbackFn();
      }
    });
  };

  /**
   * Records an event and its properties
   * @param {string} name - Name of event to be tracked
   * @param {object} properties - (optional) Properties related to the event being tracked
   * @param {function} callbackFn - (optional) Function to be called after the event is tracked.
   * @param {integer} timeout - (optional) Timeout for safe callback
   */
  var trackEvent = function (name, properties, callbackFn, timeout) {
    self.ready.done(function() {
      self.logger.debug.log(arguments, 'RECORD EVENT');
      callbackFn = Utils.createSafeCallback(callbackFn, timeout);
      _kmqPushCommand('record', properties, callbackFn, name);
    }).fail(function() {
      if (_.isFunction(callbackFn)) {
        callbackFn();
      }
    });
  };

  /**
   * Tags an HTML element to record an event when its clicked
   * @param {string} selector - The ID or class of the element to track.
   * @param {string} name - The name of the event to record.
   * @param {object} properties - optional Properties related to the event being recorded.
   */
  var internalClick = function (selector, name, properties) {
    self.ready.done(function() {
      self.logger.debug.log(self.logger.fmt.labelArgs(["Selector", "Name", "Properties"], arguments), 'Track Internal Click');
      _kmqPushCommand('trackClick', properties, undefined, name);
    });
  };

  /**
   * Tags a link that takes someone to another domain and provides enough time to record an event when the link is clicked, before being redirected.
   * @param {string} selector - The ID or class of the element to track.
   * @param {string} name - The name of the event to record.
   * @param {object} properties - optional Properties related to the event being recorded.
   */
  var trackOutboundLink = function (selector, name, properties) {
    self.ready.done(function() {
      self.logger.debug.log(self.logger.fmt.labelArgs(["Selector", "Name", "Properties"], arguments), 'Track Click on Outbound Link');
      _kmqPushCommand('trackClickOnOutboundLink', properties, undefined, name);
    });
  };


  /**
   * Fetches value for a given AB Test.
   * @param testSlug
   * @returns {*|{}}
   */
  var getAbTest = function (testSlug) {
    return _allAbTests[testSlug];
  };


  /**
   * Run some code once all data and scripts are loaded.
   * @param callback
   * @returns Nothing
   */
  var whenReadyAlways = function(callback) {
    self.ready.always(callback);
  };


  var bindEvents = function () {

    _.each($('[data-kmq="true"]'), function ($elem) {

      $elem = $($elem);

      var name = $elem.attr('data-kmq-name'),
          properties = $.parseJSON($elem.attr('data-kmq-properties') || "{}");

      internalClick('#' + $elem.attr('id'), name, properties);

    });

    _.each($('[data-kmq-external="true"]'), function ($elem) {

      $elem = $($elem);
      
      var name = $elem.attr('data-kmq-name'),
          properties = $.parseJSON($elem.attr('data-kmq-properties') || "{}");

      trackOutboundLink('#' + $elem.attr('id'), name, properties);

    });

  };


  return {
    initialize: function () {
      var apiId = Utils.getApiId('KISSMETRICS'),
          scriptUrls = [
            '//i.kissmetrics.com/i.js',
            '//scripts.kissmetrics.com/' + apiId + '.2.js',
          ];

      self.logger = Logging.getLoggerForApi('Kissmetrics');
      self.ready = $.Deferred();
      self.ready = Utils.initApi(self.ready, apiId, scriptUrls, self.logger, function() {
        // Identify user and HQ instance
        // This needs to happen before any events are sent or any traits are set
        var username = Utils.getConfig('userId');
        if (username) {
          var traits = {};
          identifyTraits(traits);
        }

        // Initialize AB Tests
        var abTests = Utils.getAbTests();
        _.each(abTests, function (ab) {
          var test = {};
          if (_.isObject(ab) && ab.version) {
            test[ab.name] = ab.version;
            self.logger.debug.log(test, ["AB Test", "New Test: " + ab.name]);
            _kmqPushCommand('set', test);
            _.extend(_allAbTests, test);
          }
        });

        bindEvents();
      });

      self.ready.done(function () {
        $('.cta-schedule-demo').click(function () {
          var clickClass = $(this).data('clickclass');
          trackEvent("Demo Workflow - Dimagi.com Button Clicked - " + clickClass);
        });
      });

    },
    identify: identify,
    identifyTraits: identifyTraits,
    track: {
      event: trackEvent,
      internalClick: internalClick,
      outboundLink: trackOutboundLink,
    },
    getAbTest: getAbTest,
    whenReadyAlways: whenReadyAlways,
  };
});
