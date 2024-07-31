from setuptools import setup, find_packages

version = "0.1"

setup(
    name="ckanext-dap",
    version=version,
    description="Add Digital Analytics Program (DAP) tracking to a CKAN instance",
    long_description="""The United States Federal Government tracks use of its websites through
    the Digital Analytics Program, with file downloads separately tracked from web pages. This CKAN extension
    simplifies embedding the appropriate Javascript code in CKAN web pages to implement DAP
    tracking, and explicitly tracking access to Resources through a CKAN instance.
	""",
    classifiers=['Development Status :: 2 - Pre-Alpha','Environment :: Plugins',
    'Programming Language :: Python :: 3'],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="",
    author="Keith Tucker",
    author_email="keith.tucker@ed.gov",
    url="",
    license="CC BY",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    namespace_packages=["ckanext", "ckanext.dap"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points="""
        [ckan.plugins]
	# Add plugins here, eg
	dap=ckanext.dap.plugin:DAPPlugin
	""",
)
