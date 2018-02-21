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

  var jobUrl = $("meta[property='dimagi:jobUrl']").attr("content");

  var Job = function (id, role, type, team, location) {
    var job = this;
    job.id = id;
    job.url = ko.observable(jobUrl.replace('12345678', id));
    job.role = ko.observable(role);
    job.type = ko.observable(type);
    job.team = ko.observable(team);
    job.location = ko.observable(location);
  };

  return {
    createJob: function (id, role, type, team, location) {
      return new Job(id, role, type, team, location);
    },
  };
});
