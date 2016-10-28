|Logo|

py-make
=======

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

    pip install py-make

Latest development release on github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|GitHub-Status| |GitHub-Stars| |GitHub-Forks|

Pull and install in the current directory:

.. code:: sh

    pip install -e git+https://github.com/tqdm/py-make.git@master#egg=py-make


Changelog
---------

The list of all changes is available either on GitHub's Releases:
|GitHub-Status| or on crawlers such as
`allmychanges.com <https://allmychanges.com/p/python/py-make/>`_.


Usage
-----

Simply install then execute ``pymake`` in a directory containing a ``Makefile``.


Known Issues
------------

For compatibility, ensure:

1. Every alias is preceded by @[+]make (eg: @make alias)
2. A maximum of one @make alias or command per line

A full list of what is and is not supported is on the
`issue tracker <https://github.com/tqdm/py-make/issues/1>`__.

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

All source code is hosted on `GitHub <https://github.com/tqdm/py-make>`__.
Contributions are welcome.

See the
`CONTRIBUTE <https://raw.githubusercontent.com/tqdm/py-make/master/CONTRIBUTE>`__
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

.. |Logo| image:: https://raw.githubusercontent.com/tqdm/py-make/master/logo.png
.. |Screenshot| image:: https://raw.githubusercontent.com/tqdm/py-make/master/images/py-make.gif
.. |Build-Status| image:: https://travis-ci.org/tqdm/py-make.svg?branch=master
   :target: https://travis-ci.org/tqdm/py-make
.. |Coverage-Status| image:: https://coveralls.io/repos/tqdm/py-make/badge.svg
   :target: https://coveralls.io/r/tqdm/py-make
.. |Branch-Coverage-Status| image:: https://codecov.io/github/tqdm/py-make/coverage.svg?branch=master
   :target: https://codecov.io/github/tqdm/py-make?branch=master
.. |GitHub-Status| image:: https://img.shields.io/github/tag/tqdm/py-make.svg?maxAge=2592000
   :target: https://github.com/tqdm/py-make/releases
.. |GitHub-Forks| image:: https://img.shields.io/github/forks/tqdm/py-make.svg
   :target: https://github.com/tqdm/py-make/network
.. |GitHub-Stars| image:: https://img.shields.io/github/stars/tqdm/py-make.svg
   :target: https://github.com/tqdm/py-make/stargazers
.. |PyPI-Status| image:: https://img.shields.io/pypi/v/py-make.svg
   :target: https://pypi.python.org/pypi/py-make
.. |PyPI-Downloads| image:: https://img.shields.io/pypi/dm/py-make.svg
   :target: https://pypi.python.org/pypi/py-make
.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/py-make.svg
   :target: https://pypi.python.org/pypi/py-make
.. |LICENCE| image:: https://img.shields.io/pypi/l/py-make.svg
   :target: https://raw.githubusercontent.com/tqdm/py-make/master/LICENCE
.. |DOI-URI| image:: https://zenodo.org/badge/21637/tqdm/py-make.svg
   :target: https://zenodo.org/badge/latestdoi/21637/tqdm/py-make
.. |README-Hits| image:: http://hitt.herokuapp.com/pymake/pymake.svg
