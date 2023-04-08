const path = require("path");

module.exports = [
  {
    entry: "./js/materialsymbols.js",
    output: {
      filename: "custom_components/materialsymbols/materialsymbols.js",
      path: path.resolve(__dirname),
    },
    mode: "production",
  },
];
