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
          contactFormId = $("meta[property='dimagi:contactFormId']").attr('content'),
          scriptUrls = [
            '//js.hsforms.net/forms/v2.js',
          ];

      if (contactFormId && apiId) {
        $.when.apply($, _.map(scriptUrls, function(url) { return $.getScript(url); }))
          .done(function() {
            hbspt.forms.create({
              portalId: apiId,
              formId: contactFormId,
              target: "#contact-form-content",
              css: ""
            });
          });
      }

    },
  };
});
