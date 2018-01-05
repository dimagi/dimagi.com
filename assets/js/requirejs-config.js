requirejs.config({
  baseUrl: document.querySelector("meta[property='dimagi:baseUrl']").getAttribute("content") + 'js/',
  paths: {
    "jquery": "lib/jquery/jquery.min",
    "knockout": "lib/knockout/knockout-latest",
    "blazy": "lib/blazy/blazy",
    "lodash": "lib/lodash/lodash"
  },
  shim: {
  },
  map: {
  },
});
