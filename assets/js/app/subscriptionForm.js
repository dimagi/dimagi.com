/* globals hbspt */
define([
  'jquery',
  'app/analytix/hubspot',
], function (
    $,
    hubspot
) {
  'use strict';
  var self = {};

  self.loadsubScriptionForm = function () {
    var apiId = hubspot.apiId(),
    subscriptionFormId = $("meta[property='dimagi:subscriptionFormId']").attr('content');

    if (subscriptionFormId) {
      hbspt.forms.create({
        portalId: apiId,
        formId: subscriptionFormId,
        target: "#email-subscribtion-form-content",
        css: ""
      });
    }
  };

  return {
    initialize: function () {
      $(function () {
        hubspot.onFormsReady(self.loadsubScriptionForm);
      });
    },
  };
});
