requirejs.config({
    paths: {
        jquery: "lib/jquery/jquery.min",
        lodash: "lib/lodash/lodash.min",
        knockout: "lib/knockout/knockout-latest"
    }
});

require([
    'jquery',
], function (
    $
) {
    'use strict';

    var referralUrl = $("meta[property='dimagi:referralUpdateUrl']").attr('content'),
        csrftoken = $("[name=csrfmiddlewaretoken]").val();

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    window.friendbuy = window.friendbuy || [];

    $(function () {
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        window.friendbuy.push(['subscribe', 'share.success',
            function (share) {
                $.post(referralUrl, share);
            }
        ]);
    });
});
