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
          demoFormId = $("meta[property='dimagi:demoFormId']").attr('content'),
          currentUrl = document.location.href;

      if (currentUrl.indexOf('?email=') !== -1) {
        window.history.pushState(
            "dimagi.com " + document.title, document.title, currentUrl.split('?')[0]
        );
      }

      if (demoFormId && apiId) {
        hbspt.forms.create({
          portalId: apiId,
          formId: demoFormId,
          target: "#demo-form-content",
          css: "",
          onFormSubmit: function ($form) {
            $('#demo-calendar-content').fadeIn();
            $('#demo-form-content').addClass('hide');
            var email = $form.find('[name="email"]').val(),
                firstname = $form.find('[name="firstname"]').val(),
                lastname = $form.find('[name="lastname"]').val(),
                newUrl = document.location.href + '?email=' + email + '&name=' + firstname + '%20' + lastname;

            window.history.pushState(
                "dimagi-contact-url " + document.title, document.title, newUrl
            );

            $.getScript('//cdn.scheduleonce.com/mergedjs/so.js');

          },
        });
      }

    },
  };
});
