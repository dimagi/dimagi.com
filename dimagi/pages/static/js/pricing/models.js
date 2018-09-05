define([
  'knockout',
  'lodash',
  'jquery',
], function (
  ko,
  _,
  $
) {
  'use strict';

  var Price = function (yearly, monthly, page) {
    var p = this;
    p.monthly = ko.observable(monthly);
    p.yearly = ko.observable(yearly);

    p.displayPrice = ko.computed(function () {
      if (page.showMonthly()) {
        return p.monthly();
      }
      return p.yearly();
    });

  };

  var PricingPage = function () {
    var page = this;

    page.showMonthly = ko.observable(false);

    page.paymentType = ko.computed(function () {
      if (page.showMonthly()) {
        return "Paying Monthly";
      }
      return "Paying Annually";
    });

    page.standard = new Price(250, 300, page);
    page.pro = new Price(500, 600, page);
    page.advanced = new Price(1000, 1200, page);

  };

  return {
    createPricingPage: function () {
      return new PricingPage();
    },
  };
});
