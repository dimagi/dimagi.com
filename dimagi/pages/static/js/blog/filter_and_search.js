define([
  'lodash',
  'jquery',
  'knockout',
  'select2',
], function (
  _,
  $,
  ko
) {
  'use strict';

  ko.bindingHandlers.select2Update = {
    update: function (element, valueAccessor, allBindingsAccessor) {
        var allBindings = allBindingsAccessor();
        // need this line to ensure update is called when the selectedOptions refreshes
        ko.utils.unwrapObservable(allBindings.selectedOptions);

        var select2 = $(element).data('select2');
        if (select2) {
          // ensure that the UI stays updated if the value of the select element changes due to ko
          $(element).trigger('change.select2');
        }
    },
  };

  var filterAndSearch = function (options) {
    var self = {};

    self.categories = ko.observableArray(options.filter.categories);
    self.tags = ko.observableArray(options.filter.tags);

    self.searchCategory = ko.observable(options.initial.category || 'all');
    self.searchTags = ko.observableArray(options.initial.tags || []);
    self.searchTerm = ko.observable(options.initial.term || '');

    self.showFilters = ko.observable(false);

    self.hasFilters = ko.computed(function () {
      return self.searchTags().length > 0 || self.searchCategory() !== 'all';
    });

    self.showHasFiltersAlert = ko.computed(function () {
      return self.hasFilters() && !self.showFilters();
    });

    self.submitSearchOnEnter = function (d, e) {
      if (e.keyCode === 13 && self.searchTerm()) {
        self.submitSearch();
      }
      return true;
    };

    self.toggleFilters = function () {
      self.showFilters(!self.showFilters());
    };

    self.closeFilters = function () {
      self.showFilters(false);
    };

    self.getCategoryUrl = function (slug) {
      var category = _.find(self.categories(), function (c) {
        return c.slug === slug;
      });
      return category.url;
    };

    self.submitSearch = function () {
      var url = self.getCategoryUrl(self.searchCategory()),
          query = {
            s: self.searchTerm(),
            t: _.join(self.searchTags(), ','),
          };
      window.location = url + '?' + $.param(query);

    };

    self.activate = function($parentNav) {
      var select2Options = {
        placeholder: "Select Tags...",
        width: '100%',
      };

      if ($parentNav.hasClass('sub-nav-fixed')) {
        $parentNav.find('#filter-tags').get(0).id = 'filter-tags-fixed';
        $parentNav.find('#filter-tags-fixed').select2(select2Options);
      } else {
        $parentNav.find('#filter-tags').select2(select2Options);
      }
    };

    return self;
  };


  return {
    getFilterAndSearchModel: function (options) {
      return new filterAndSearch(options);
    },
  };
});

