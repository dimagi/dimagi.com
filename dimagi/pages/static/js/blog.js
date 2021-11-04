requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min",
    knockout: "lib/knockout/knockout-latest",
    select2: "lib/select2/dist/js/select2.min"
  }
});

require([
  'jquery',
  'lodash',
  'knockout',
  'blog/filter_and_search',
], function (
  $,
  _,
  ko,
  filterAndSearch
) {
  'use strict';
  $(function () {
      var options = {
            filter: $.parseJSON($("meta[property='dimagi:blogFilters']").attr('content')),
            initial: {},
          },
          $existingFilters = $("meta[property='dimagi:existingBlogFilters']"),
          model;
      if ($existingFilters.length > 0) {
        options.initial = $.parseJSON($existingFilters.attr('content'));
      }
      model = filterAndSearch.getFilterAndSearchModel(options);
      window.subNavKoModel = model;
      ko.applyBindings(model, $('#sub-nav').get(0));
  });
});
