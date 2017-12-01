requirejs.config({
  baseUrl: '/static/js/',
  paths: {
    "lib/jquery": "lib/jquery/dist/jquery.min",
    "lib/knockout": "lib/knockout/build/output/knockout-latest",
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
