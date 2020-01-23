define([
  'knockout',
  'lodash',
  'jquery',
  'careers/models',
], function (
  ko,
  _,
  $,
  Models
) {
  'use strict';
  var self = {};

  self.jobsBy = {
    location: {},
    team: {},
    role: {},
    type: {},
  };

  self.allJobs = [];

  self.current = {};

  function _addJob(key, value, job) {
    if (self.jobsBy[key][value] === undefined) {
      self.jobsBy[key][value] = [];
    }
    self.jobsBy[key][value].push(job);
    self.allJobs.push(job);
  }

  return {
    initialize: function () {
      $.get('https://api.greenhouse.io/v1/boards/dimagi/offices', function (data) {
        var fields = {};

        _.forEach(data.offices, function (office) {
          fields.location = office.location;

          _.forEach(office.departments, function (department) {
            fields.team = department.name;

            _.forEach(department.jobs, function (job) {
              fields.role = job.title;
              fields.type = "Full-time"; // default value if no metadata found
              _.forEach(job.metadata, function (meta) {
                if (meta.name === 'Employment Type') {
                  fields.type = meta.value;
                }
              });

              _.forEach(fields, function (value, key) {
                _addJob(key, value, Models.createJob(
                    job.id,
                    fields.role,
                    fields.type,
                    fields.team,
                    job.location.name
                ));
              });

            }); // foreach jobs
          }); // foreach department
        }); // foreach offices


        self.roles = ko.observableArray(_.keys(self.jobsBy.role));
        self.currentRole = ko.observable('');

        self.teams = ko.observableArray(_.keys(self.jobsBy.team));
        self.currentTeam = ko.observable('');

        self.types = ko.observableArray(_.keys(self.jobsBy.type));
        self.currentType = ko.observable('');

        self.locations = ko.observableArray(_.keys(self.jobsBy.location));
        self.currentLocation = ko.observable('');

        self.allJobs = _.uniqBy(self.allJobs, 'id');

        self.jobs = ko.computed(function () {
          var jobs = self.allJobs;

          if (self.currentRole()) {
            jobs = _.intersectionBy(jobs, self.jobsBy.role[self.currentRole()], 'id');
          }
          if (self.currentTeam()) {
            jobs = _.intersectionBy(jobs, self.jobsBy.team[self.currentTeam()], 'id');
          }
          if (self.currentType()) {
            jobs = _.intersectionBy(jobs, self.jobsBy.type[self.currentType()], 'id');
          }
          if (self.currentLocation()) {
            jobs = _.intersectionBy(jobs, self.jobsBy.location[self.currentLocation()], 'id');
          }

          return _.uniqBy(jobs, 'id');
        });

        ko.applyBindings(self, document.getElementById('open-positions'));

      });
    },
  };
});
