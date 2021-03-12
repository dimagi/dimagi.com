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
    'app/analytix/kissmetrix',
], function (
    $,
    _,
    Utils,
    Logging,
    Hubspot,
    kissmetrics
) {
    'use strict';
    var self = {},
        _drift = window.drift || {};
    return {
        initialize: function () {
            self.hideDrift = $("meta[property='dimagi:driftHide']").attr("content");
            if (self.hideDrift) return;
            if (_.isEmpty(_drift)) return;

            _drift.on('emailCapture',function(e){
                Hubspot.identify({email: e.data.email});
                Hubspot.trackEvent('Identified via Drift');
            });

            $('.cta-schedule-demo-drift').click(function (e) {
                var hasInteracted = false;
                e.preventDefault();

                window.drift.on('startConversation', function () {
                    kissmetrics.track.event("Demo Workflow - Viewed Form");
                });

                window.drift.on("emailCapture", function () {
                    kissmetrics.track.event("Demo Workflow - Contact Info Received");
                    kissmetrics.track.event("Demo Workflow - Loaded Booking Options");
                });

                window.drift.on("sliderMessage:close", function () {
                    kissmetrics.track.event("Demo Workflow - Dismissed Form");
                    window.drift.off("sliderMessage:close");
                });

                window.drift.on("scheduling:meetingBooked", function () {
                    kissmetrics.track.event("Demo Workflow - Demo Scheduled");
                    window.drift.off("sliderMessage:close");
                });

                window.drift.on("message:sent", function () {
                    if (!hasInteracted) {
                        hasInteracted = true;
                        kissmetrics.track.event("Demo Workflow - Interacted With Form");
                    }
                    window.drift.off("message:sent");
                });

                if (window.drift.api) {
                    window.drift.api.startInteraction({
                        interactionId: 43079,
                        goToConversation: true,
                    });
                }
            });

        },
    };
});
