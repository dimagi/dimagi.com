/* globals STATIC_CDN */
requirejs.config({
  baseUrl: STATIC_CDN + '/static/js/',
  paths: {
    "lib/jquery": "lib/jquery/jquery.min",
    "lib/knockout": "lib/knockout/knockout-latest",
    "lib/blazy": "lib/blazy/blazy",
    "lib/lodash": "lib/lodash/lodash"
  },

  // todo use compilation from requirejs.yaml like hq
  modules: [
    {
      name: "common",
      include: [
        "lib/jquery",
        "lib/knockout",
        "lib/blazy",
        "lib/lodash",
      ]
    }
  ],
  shim: {
  },
  map: {
  },
});
