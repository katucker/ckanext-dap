// Add Digital Analytics Program event tracking to resource download links.
this.ckan.module("dap", function(jQuery, _) {
  "use strict";
  return {
    initialize: function() {
      jQuery("a.resource-url-analytics").on("click", function() {
        var resource_url = encodeURIComponent(jQuery(this).prop("href"));
        if (resource_url) {
          gas("send", "event", "data asset", "file_download", resource_url);
        }
      });
    }
  };
});
