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

    if ($('.home-child-health')) {
        $(document).ready(function (e) {
            $('.sector-sub-intro').addClass('hide');
        });
    }

    $('.home-all-sectors').click(function (e) {
        $('.child-blue-theme').removeClass('hide');
        $('.child-green-theme').removeClass('hide');
        $('.child-purple-theme').removeClass('hide');
        $('.child-red-theme').removeClass('hide');
        $('.sector-sub-intro').addClass('hide');
        $('.sectors-intro-main').removeClass('hide');
    });

    $('.home-child-health').click(function (e) {
        $('.child-blue-theme').removeClass('hide');
        $('.child-turquoise-theme').addClass('hide');
        $('.child-green-theme').addClass('hide');
        $('.child-purple-theme').addClass('hide');
        $('.child-red-theme').addClass('hide');
        $('.sector-sub-intro').removeClass('hide');
        $('.sectors-intro-main').addClass('hide');
    });

    $('.home-agricultural-programs').click(function (e) {
        $('.child-green-theme').removeClass('hide');
        $('.child-turquoise-theme').addClass('hide');
        $('.child-blue-theme').addClass('hide');
        $('.child-purple-theme').addClass('hide');
        $('.child-red-theme').addClass('hide');
        $('.sector-sub-intro').removeClass('hide');
        $('.sectors-intro-main').addClass('hide');
    });

    $('.home-community-development').click(function (e) {
        $('.child-purple-theme').removeClass('hide');
        $('.child-turquoise-theme').addClass('hide');
        $('.child-blue-theme').addClass('hide');
        $('.child-green-theme').addClass('hide');
        $('.child-red-theme').addClass('hide');
        $('.sector-sub-intro').removeClass('hide');
        $('.sectors-intro-main').addClass('hide');
    });

    $('.home-urgent-response').click(function (e) {
        $('.child-red-theme').removeClass('hide');
        $('.child-turquoise-theme').addClass('hide');
        $('.child-blue-theme').addClass('hide');
        $('.child-purple-theme').addClass('hide');
        $('.child-green-theme').addClass('hide');
        $('.sector-sub-intro').removeClass('hide');
        $('.sectors-intro-main').addClass('hide');
    });

});
