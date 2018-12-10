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

    self.loadContactForm = function () {
        var apiId = hubspot.apiId(),
            contactFormId = $("meta[property='dimagi:contactFormId']").attr('content');

        if (contactFormId) {
            hbspt.forms.create({
                portalId: apiId,
                formId: contactFormId,
                target: "#contact-form-content",
                css: ""
            });
        }
    };

    return {
        initialize: function () {
            $(function () {
                hubspot.onFormsReady(self.loadContactForm);
            });
        },
    };
});
