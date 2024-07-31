import pytest

import ckan.logic as logic
import ckan.tests.factories as factories
import ckan.tests.helpers as helpers

@pytest.mark.ckan_config('ckan.plugins',  'dap')
@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')

def test_dap_link(app):
    # Check that the link is embedded in the main page content.
    main = app.get('/')

    assert main.find('Universal-Federated-Analytics') != -1

from ../dap/plugin.py import DigitalAnalyticsProgramException

@helpers.change_config('ckanext.dap.agency', None)
def test_agency_required(config):
    with DigitalAnalyticsProgramException:
        _ = config.get('ckanext.dap.agency')