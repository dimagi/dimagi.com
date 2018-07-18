/* global console */
define([
  'jquery',
  'lodash',
], function (
    $,
    _
) {
  'use strict';
  var self = {};
  self.curClasses = [];

  self.auditClicks = function () {

    var subnavDupes,
        otherClasses,
        duplicates;

    $('a').each(function (index, link) {
      var cssClass = $(link).attr('class'),
          content = $(link).text().trim();
      if (_.isUndefined(cssClass) && !_.isEmpty(content)) {
        console.log("Missing AB Click Class: " + content);
      } else if (cssClass && cssClass.indexOf('ab-') < 0 && !_.isEmpty(content)) {
        console.log("Missing AB Click Class: " + content + " (" + cssClass + ")");
      } else if (cssClass && cssClass.indexOf('ab-') >= 0) {
        self.curClasses.push(cssClass.match(/ab[\w-]*\b/)[0]);
      }
    });

    subnavDupes = _(self.curClasses).filter(function (x) {
      return x.indexOf('ab-subnav-') >= 0;
    }).groupBy().pickBy(x => x.length > 2).keys().value();
    duplicates = _(self.curClasses).filter(function (x) {
      return x.indexOf('ab-subnav-') < 0;
    }).groupBy().pickBy(x => x.length > 1).keys().value();

    duplicates = _.union(duplicates, subnavDupes);
    console.log("Duplicates:");
    console.log(duplicates);

  };

  return {
    initialize: function () {

      if($("meta[property='dimagi:auditABClicks']").attr("content")) {
        self.auditClicks();
      }

    },
  };
});
