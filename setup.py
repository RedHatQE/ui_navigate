from setuptools import setup, find_packages
setup(
    name="ui_navigate",
    version="1.0.1",
    packages=find_packages(),
    #scripts=['say_hello.py'],

    # metadata for upload to PyPI
    author="Jeff Weiss",
    author_email="jweiss@redhat.com",
    description="UI navigation library for automation",
    license="PSF",
    keywords="automation navigation gui selenium",
    url="https://github.com/RedHatQE/ui_navigate",

    # could also include long_description, download_url, classifiers, etc.
)
