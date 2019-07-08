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
            $('.child-green-theme').addClass('hide');
            $('.child-purple-theme').addClass('hide');
            $('.child-red-theme').addClass('hide');
            $('.home-agricultural-programs').addClass('sector-home-inactive');
            $('.home-community-development').addClass('sector-home-inactive');
            $('.home-urgent-response').addClass('sector-home-inactive');
        });
    }

    $('.home-child-health').click(function (e) {
        $('.child-blue-theme').removeClass('hide');
        $('.child-green-theme').addClass('hide');
        $('.child-purple-theme').addClass('hide');
        $('.child-red-theme').addClass('hide');
        $('.home-child-health').removeClass('sector-home-inactive');
        $('.home-agricultural-programs').addClass('sector-home-inactive');
        $('.home-community-development').addClass('sector-home-inactive');
        $('.home-urgent-response').addClass('sector-home-inactive');
    });

    $('.home-agricultural-programs').click(function (e) {
        $('.child-green-theme').removeClass('hide');
        $('.child-blue-theme').addClass('hide');
        $('.child-purple-theme').addClass('hide');
        $('.child-red-theme').addClass('hide');
        $('.home-agricultural-programs').removeClass('sector-home-inactive');
        $('.home-child-health').addClass('sector-home-inactive');
        $('.home-community-development').addClass('sector-home-inactive');
        $('.home-urgent-response').addClass('sector-home-inactive');
    });

    $('.home-community-development').click(function (e) {
        $('.child-purple-theme').removeClass('hide');
        $('.child-blue-theme').addClass('hide');
        $('.child-green-theme').addClass('hide');
        $('.child-red-theme').addClass('hide');
        $('.home-community-development').removeClass('sector-home-inactive');
        $('.home-agricultural-programs').addClass('sector-home-inactive');
        $('.home-child-health').addClass('sector-home-inactive');
        $('.home-urgent-response').addClass('sector-home-inactive');
    });

    $('.home-urgent-response').click(function (e) {
        $('.child-red-theme').removeClass('hide');
        $('.child-blue-theme').addClass('hide');
        $('.child-purple-theme').addClass('hide');
        $('.child-green-theme').addClass('hide');
        $('.home-urgent-response').removeClass('sector-home-inactive');
        $('.home-agricultural-programs').addClass('sector-home-inactive');
        $('.home-community-development').addClass('sector-home-inactive');
        $('.home-child-health').addClass('sector-home-inactive');
        $('.home-urgent-response').removeClass('sector-home-inactive');
    });

});
