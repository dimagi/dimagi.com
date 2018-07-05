/* globals hbspt */
define([
  'jquery',
  'app/analytix/utils',
], function (
    $,
    Utils
) {
  'use strict';

  return {
    initialize: function () {
      var apiId = Utils.getApiId('HUBSPOT'),
          contactFormId = $("meta[property='dimagi:contactFormId']").attr('content');

      if (contactFormId && apiId) {
        hbspt.forms.create({
          portalId: apiId,
          formId: contactFormId,
          target: "#contact-form-content",
          css: ""
        });
      }

    },
  };
});
