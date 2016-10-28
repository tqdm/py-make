|Logo|

pymake
======

|PyPI-Status| |PyPI-Versions|

|Build-Status| |Coverage-Status| |Branch-Coverage-Status|

|LICENCE|


Bring basic ``Makefile`` support to any system with Python.

Inspired by work in `tqdm <https://github.com/tqdm/tqdm>`__.

Simply install then execute ``pymake`` in a directory containing a ``Makefile``.

``pyamke`` works on any platform (Linux, Windows, Mac, FreeBSD, Solaris/SunOS).

``pymake`` does not require any library to run, just a vanilla Python
interpreter will do.

------------------------------------------

.. contents:: Table of contents
   :backlinks: top
   :local:


Installation
------------

Latest PyPI stable release
~~~~~~~~~~~~~~~~~~~~~~~~~~

|PyPI-Status|

.. code:: sh

    pip install pymake

Latest development release on github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|GitHub-Status| |GitHub-Stars| |GitHub-Forks|

Pull and install in the current directory:

.. code:: sh

    pip install -e git+https://github.com/tqdm/pymake.git@master#egg=pymake


Changelog
---------

The list of all changes is available either on GitHub's Releases:
|GitHub-Status| or on crawlers such as
`allmychanges.com <https://allmychanges.com/p/python/pymake/>`_.


Usage
-----

Simply install then execute ``pymake`` in a directory containing a ``Makefile``.


Known Issues
------------

For compatibility, ensure:

1. Every alias is preceded by @[+]make (eg: @make alias)
2. A maximum of one @make alias or command per line

Sample makefile compatible with ``pymake``:

.. code:: sh

    all:
    	@make test
    	@make install
    test:
    	nosetest
    install:
    	python setup.py install


Documentation
-------------

|PyPI-Versions| |README-Hits| (Since 19 May 2016)

.. code:: sh

    pymake --help


Contributions
-------------

All source code is hosted on `GitHub <https://github.com/tqdm/pymake>`__.
Contributions are welcome.

See the
`CONTRIBUTE <https://raw.githubusercontent.com/tqdm/pymake/master/CONTRIBUTE>`__
file for more information.


LICENCE
-------

Open Source (OSI approved): |LICENCE|

Citation information: |DOI-URI|


Authors
-------

-  Casper da Costa-Luis (casperdcl)*
-  Stephen Larroque (lrq3000)*

|README-Hits| (Since 28 Oct 2016)

.. |Logo| image:: https://raw.githubusercontent.com/tqdm/pymake/master/logo.png
.. |Screenshot| image:: https://raw.githubusercontent.com/tqdm/pymake/master/images/pymake.gif
.. |Build-Status| image:: https://travis-ci.org/tqdm/pymake.svg?branch=master
   :target: https://travis-ci.org/tqdm/pymake
.. |Coverage-Status| image:: https://coveralls.io/repos/tqdm/pymake/badge.svg
   :target: https://coveralls.io/r/tqdm/pymake
.. |Branch-Coverage-Status| image:: https://codecov.io/github/tqdm/pymake/coverage.svg?branch=master
   :target: https://codecov.io/github/tqdm/pymake?branch=master
.. |GitHub-Status| image:: https://img.shields.io/github/tag/tqdm/pymake.svg?maxAge=2592000
   :target: https://github.com/tqdm/pymake/releases
.. |GitHub-Forks| image:: https://img.shields.io/github/forks/tqdm/pymake.svg
   :target: https://github.com/tqdm/pymake/network
.. |GitHub-Stars| image:: https://img.shields.io/github/stars/tqdm/pymake.svg
   :target: https://github.com/tqdm/pymake/stargazers
.. |PyPI-Status| image:: https://img.shields.io/pypi/v/pymake.svg
   :target: https://pypi.python.org/pypi/pymake
.. |PyPI-Downloads| image:: https://img.shields.io/pypi/dm/pymake.svg
   :target: https://pypi.python.org/pypi/pymake
.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/pymake.svg
   :target: https://pypi.python.org/pypi/pymake
.. |LICENCE| image:: https://img.shields.io/pypi/l/pymake.svg
   :target: https://raw.githubusercontent.com/tqdm/pymake/master/LICENCE
.. |DOI-URI| image:: https://zenodo.org/badge/21637/tqdm/pymake.svg
   :target: https://zenodo.org/badge/latestdoi/21637/tqdm/pymake
.. |Screenshot-Jupyter1| image:: https://raw.githubusercontent.com/tqdm/pymake/master/images/pymake-jupyter-1.gif
.. |Screenshot-Jupyter2| image:: https://raw.githubusercontent.com/tqdm/pymake/master/images/pymake-jupyter-2.gif
.. |Screenshot-Jupyter3| image:: https://raw.githubusercontent.com/tqdm/pymake/master/images/pymake-jupyter-3.gif
.. |README-Hits| image:: http://hitt.herokuapp.com/tqdm/pymake.svg
