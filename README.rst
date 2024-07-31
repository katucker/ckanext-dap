CKAN Digital Analytics Program Tracking Extension
===============================

**Status:** Production

**CKAN Version:** >= 2.9.*

A CKAN extension that sends tracking data to the United States Federal Government's 
Digital Analytics Program (DAP).

Features
--------

* Puts the DAP asynchronous tracking code into page headers
  for basic page tracking.

* Complies with DAP protocol to only track anonymously-accessed web pages.

* Supports automated tracking of resource file downloads, regardless of whether the 
resource is stored in the CKAN instance or merely referenced by it.

Installation
------------

1. Install the extension as usual, e.g. (from an activated virtualenv):

    ::

    $ pip install -e  git+https://github.com/katucker/ckanext-dap.git
    $ pip install -r ckanext-dap/requirements.txt

2. Edit your ckan.ini (or similar) to provide the parameters below for 
constructing the tracking link.

    ::
    Required tracking parameters:
        ckanext.dap.agency = <Agency name, used to segregate DAP tracking 
            events. Must match an agency name defined in the GSA DAP
            documentation at 
            https://github.com/digital-analytics-program/gov-wide-code>

    Optional tracking parameters:
        ckanext.dap.subagency = <Name of subordinate agency, for further 
            segregating tracking events.>
        ckanext.dap.topic <Short description of the site's topic, used
            for distinguishing specific content from other
            agency/subagency content or across agencies.>
        ckanext.dap.platform = <Specifices a name under which multiple
            sites may be hosted, such as cloud.gov.>
        ckanext.dap.search = <List of parameter names that are used to
            initiate searches on the site. Used to categorize URLs
            containing the terms as searches. See the DAP documentation
            for the list of default search paramenter names. The CKAN standard
            query parameters are already tracked by DAP, so this parameter is
            only needed for CKAN instances that implement custom searches with
            other search terms.>
        ckanext.dap.extensions = <List of additional file extensions for tracking
            file downloads for other than package resources (such as embedded
            in the description text for a package or resource). This extension embeds
            tracking code in the resource hyperlinks, so all resources downloads are tracked
            no matter what the file extension is.
            See the GSA DAP documentation for a list of file extensions tracked by default.>
        ckanext.dap.dev = true <Enables sending tracking events to the DAP
            development database.>

3. Add the extension to the list of plugins in the ini file,
   such as the following:

   ::

      ckan.plugins = dap dapr

   (The dapr extension is a separate CKAN extension, shown here
   to illustrate specifying multiple CKAN extensions.)


4. Restart CKAN (e.g. by restarting Apache)

