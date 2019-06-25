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

    self.loadScheduleForm = function () {
        var apiId = hubspot.apiId(),
            scheduleFormId = $("meta[property='dimagi:scheduleFormId']").attr('content');

        if (scheduleFormId) {
            hbspt.forms.create({
                portalId: apiId,
                formId: scheduleFormId,
                target: "#schedule-form-content",
                css: ""
            });
        }
    };

    return {
        initialize: function () {
            $(function () {
                hubspot.onFormsReady(self.loadScheduleForm);
            });
        },
    };
});
