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

    self.loadCTAs = function () {
        var apiId = hubspot.apiId(),
            ctaEvents = $.parseJSON($("meta[property='dimagi:callToActionEvents']").attr("content")),
            ctaUrls = ['//js.hscta.net/cta/current.js'];

        if (ctaEvents) {
            $.when.apply($, _.map(ctaUrls, function (url) { return $.getScript(url); }))
                .done(function () {
                    _.forEach(ctaEvents, function (ctaName, ctaId) {
                        hbspt.cta.load(apiId, ctaId, {});
                        $('#hs-cta-wrapper-' + ctaId + ' > span').click(function () {
                            hubspot.trackEvent('CTA Click for ' + ctaName);
                        });
                    });
                });
        }
    };

    return {
        initialize: function () {
            $(function () {
                hubspot.onFormsReady(self.loadCTAs);
            });
        },
    };
});
