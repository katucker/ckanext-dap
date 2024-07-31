# -*- coding: utf-8 -*-
import logging

from builtins import str, range

import ckan.lib.helpers as h
import ckan.plugins as p
from ckan.plugins.toolkit import asbool, config, get_validator

from ckan.exceptions import CkanVersionException

log = logging.getLogger(__name__)

class DigitalAnalyticsProgramException(Exception):
    pass

class DAPPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)

    def configure(self, config):
        """Load config settings for this extension from config file.

        See IConfigurable.

        """
        # Fail initialization if the agency name to use for tracking is not specified.
        if "ckanext.dap.agency" not in config:
            msg = "Missing ckanext.dap.agency in config"
            raise DigitalAnalyticsProgramException(msg)

        # Load any optional tracking parameters specified.
        self.agency = config["ckanext.dap.agency"]
        self.subagency = config.get("ckanext.dap.subagency", None)
        self.platform = config.get("ckanext.dap.platform", None)
        self.extensions = config.get("ckanext.dap.extensions", None)
        self.search = config.get("ckanext.dap.search", None)
        self.topic = config.get("ckanext.dap.topic", None)
        self.dev = asbool(config.get("ckanext.dap.dev", True))

        p.toolkit.add_resource("../assets", "ckanext-dap")

    def update_config(self, config):
        """Change the CKAN environment configuration.

        See IConfigurer.

        """
        p.toolkit.add_template_directory(config, "../templates")

    def update_config_schema(self, schema):
        """Add runtime-editable configuration parameters.

        See IConfigurer.

        """
        im = get_validator('ignore_missing')
        pi = get_validator('positive_integer')

        schema.update({
            "ckanext.dap.agency": [im],
            "ckanext.dap.subagency": [im],
            "ckanext.dap.platform": [im],
            "ckanext.dap.topic": [im]
        })

        return schema

    def get_helpers(self):
        """Return the CKAN template helper functions this plugin provides.

        See ITemplateHelpers.

        """
        return {"dap_header": self.dap_header}

    def dap_header(self):
        """Render the dap_header snippet.

        This is a template helper function that renders the
        dap_header jinja snippet. To be called from the jinja
        templates in this extension, see ITemplateHelpers.

        """

        data = {
            "dap_agency": self.agency,
            "dap_subagency": self.subagency,
            "dap_platform": self.platform,
            "dap_topic": self.topic,
            "dap_extensions": self.extensions,
            "dap_search": self.search,
            "dap_dev": self.dev
        }
        return p.toolkit.render_snippet(
            "dap/snippets/digital_analytics_program_header.html", data
        )

