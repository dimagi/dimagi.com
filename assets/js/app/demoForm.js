/* globals hbspt */
define([
    'jquery',
    'app/analytix/hubspot',
    'app/analytix/kissmetrix',
], function (
    $,
    hubspot,
    kissmetrics
) {
    'use strict';
    var self = {};

    /**
     * Loads the Hubspot Request Demo form and loads a Schedule Once Calendar
     * Widget for auto-booking an appointment as soon as the form is submitted.
     */
    self.loadDemoForm = function () {
        var apiId = hubspot.apiId(),
            demoFormId = $("meta[property='dimagi:demoFormId']").attr('content'),
            currentUrl = document.location.href;

        // Reset URL
        if (currentUrl.indexOf('?email=') !== -1) {
          window.history.pushState(
              "dimagi.com " + document.title, document.title, currentUrl.split('?')[0]
          );
        }

        // Activate Demo Form
        if (demoFormId) {
            console.log('got demo form');
            console.log(demoFormId);
            hbspt.forms.create({
                portalId: apiId,
                formId: demoFormId,
                target: "#demo-form-content",
                css: "",
                onFormReady: function () {
                    var $hubspotFormModal = $('#demo-form-modal'),
                        hasInteractedWithForm = false;

                    $hubspotFormModal.on('modal.open', function () {
                        kissmetrics.track.event("Demo Workflow - Viewed Form");
                    });

                    $hubspotFormModal.on('modal.close', function () {
                        kissmetrics.track.event("Demo Workflow - Dismissed Form");
                    });

                    $('#demo-form-content').find('input').click(function () {
                        if (!hasInteractedWithForm) {
                            kissmetrics.track.event("Demo Workflow - Interacted With Form");
                            hasInteractedWithForm = true;
                        }
                    });
                },
                onFormSubmit: function ($form) {
                    $('#demo-calendar-content').fadeIn();
                    $('#demo-form-content').addClass('hide');

                    var email = $form.find('[name="email"]').val(),
                        firstname = $form.find('[name="firstname"]').val(),
                        lastname = $form.find('[name="lastname"]').val(),
                        newUrl = document.location.href + '?email=' + email + '&name=' + firstname + '%20' + lastname;

                    kissmetrics.track.event("Demo Workflow - Contact Info Received");

                    // This nastiness is required for Schedule Once to auto-fill
                    // required fields. Sending snark the way of the S.O. devs...
                    window.history.pushState({}, document.title, newUrl);

                    // Causes the Schedule Once form to populate the element
                    // #SOIDIV_commcaredemoform as soon as it loads. Once it's
                    // loaded this does not leave the page.
                    $.getScript('//cdn.scheduleonce.com/mergedjs/so.js')
                        .done(function () {
                            kissmetrics.track.event("Demo Workflow - Loaded Booking Options");
                            setTimeout(function () {
                                // This is a bit of a hack, but the only way to detect if
                                // the Schedule Once Form was submitted on our side.
                                // The style attribute changes when the form is successfully
                                // submitted.
                                var lastKnownHeight = 0,
                                    observer = new MutationObserver(function (mutations) {
                                        mutations.forEach(function () {
                                            var newHeight = $('#SOI_commcaredemoform').height();
                                            if (newHeight > lastKnownHeight) {
                                                var coreUrl = document.location.href.split('?')[0];
                                                kissmetrics.track.event("Demo Workflow - Demo Scheduled");
                                                $('#demo-form-modal').off('modal.close');
                                                window.history.pushState({}, document.title, coreUrl);
                                            }
                                            lastKnownHeight = newHeight;

                                        });
                                    });
                                // target is the the iframe containing the schedule once form
                                var target = document.getElementById('SOI_commcaredemoform');
                                observer.observe(target, {
                                  attributes: true,
                                  attributeFilter: ['style']
                                });
                            }, 3000);
                        });
                },
          });
        }
    };

    return {
        initialize: function () {
            $(function () {
                hubspot.onFormsReady(self.loadDemoForm);
            });
        },
    };
});
