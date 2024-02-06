py-make
=======

|PyPI-Status| |PyPI-Versions|

|Build-Status| |Coverage-Status| |Branch-Coverage-Status| |Codacy-Grade| |Libraries-Rank|

|DOI-URI| |LICENCE| |OpenHub-Status|


Bring basic ``Makefile`` support to any system with Python.

Inspired by work in `tqdm <https://github.com/tqdm/tqdm>`__.

Simply install then execute ``pymake`` in a directory containing a ``Makefile``.

``pymake`` works on any platform (Linux, Windows, Mac, FreeBSD, Solaris/SunOS).

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

|PyPI-Status| |PyPI-Downloads| |Libraries-Dependents|

.. code:: sh

    pip install py-make

Latest development release on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|GitHub-Status| |GitHub-Stars| |GitHub-Commits| |GitHub-Forks| |GitHub-Updated|

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

Simply install then execute ``pymake -p`` to list commands and ``pymake <command>`` to use a command, in a directory containing a ``Makefile``.


Known Issues
------------

For compatibility, ensure:

1. Every alias is preceded by @[+]make (eg: @make alias)
2. A maximum of one @make alias or command per line

A full list of what is and is not supported is on the
`issue tracker <https://github.com/tqdm/py-make/issues/1>`__.

Sample makefile compatible with ``pymake``:

.. code:: sh

    PY=python -m py_compile
    .PHONY:
    	all
    	test
        install
        compile
    all:
    	@+make test
    	@make install
    test:
    	pytest
    install:
    	python setup.py\
        install
    compile:
    	$(PY) test.py
    circle:
    	# of life
    	circle
    empty:
    	# this is a comment

If you get a "Permission Denied" error, please check if maybe your antivirus may be preventing the launch of compiled python scripts, if the Scripts subdirectory is in the PATH, or `other issues with the Python install <https://stackoverflow.com/questions/56974927/permission-denied-trying-to-run-python-on-windows-10>`__.

Documentation
-------------

|PyPI-Versions| |README-Hits| (Since 28 Oct 2016)

.. code:: sh

    pymake --help


Contributions
-------------

|GitHub-Commits| |GitHub-Issues| |GitHub-PRs| |OpenHub-Status|

All source code is hosted on `GitHub <https://github.com/tqdm/py-make>`__.
Contributions are welcome.

See the
`CONTRIBUTING.md <https://raw.githubusercontent.com/tqdm/py-make/master/CONTRIBUTING.md>`__
file for more information.


LICENCE
-------

Open Source (OSI approved): |LICENCE|

Citation information: |DOI-URI|


Authors
-------

The main developers, ranked by surviving lines of code
(`git fame -wMC <https://github.com/casperdcl/git-fame>`__), are:

- Stephen Larroque (`lrq3000 <https://github.com/lrq3000>`__, core logic)
- Casper da Costa-Luis (`casperdcl <https://github.com/casperdcl>`__, modularization & maintenance)

We are grateful for all |GitHub-Contributions|.

|README-Hits| (Since 28 Oct 2016)

.. |Build-Status| image:: https://img.shields.io/github/actions/workflow/status/tqdm/py-make/test.yml?branch=master&label=py-make&logo=GitHub
   :target: https://github.com/tqdm/py-make/actions/workflows/test.yml
.. |Coverage-Status| image:: https://coveralls.io/repos/tqdm/py-make/badge.svg?branch=master
   :target: https://coveralls.io/github/tqdm/py-make
.. |Branch-Coverage-Status| image:: https://codecov.io/gh/tqdm/py-make/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/tqdm/py-make
.. |Codacy-Grade| image:: https://api.codacy.com/project/badge/Grade/1f1dab515f294a05af8fc45e200660e5
   :target: https://www.codacy.com/app/tqdm/py-make/dashboard
.. |GitHub-Status| image:: https://img.shields.io/github/tag/tqdm/py-make.svg?maxAge=86400&logo=github&logoColor=white
   :target: https://github.com/tqdm/py-make/releases
.. |GitHub-Forks| image:: https://img.shields.io/github/forks/tqdm/py-make.svg?logo=github&logoColor=white
   :target: https://github.com/tqdm/py-make/network
.. |GitHub-Stars| image:: https://img.shields.io/github/stars/tqdm/py-make.svg?logo=github&logoColor=white
   :target: https://github.com/tqdm/py-make/stargazers
.. |GitHub-Commits| image:: https://img.shields.io/github/commit-activity/y/tqdm/py-make.svg?logo=git&logoColor=white
   :target: https://github.com/tqdm/py-make/graphs/commit-activity
.. |GitHub-Issues| image:: https://img.shields.io/github/issues-closed/tqdm/py-make.svg?logo=github&logoColor=white
   :target: https://github.com/tqdm/py-make/issues
.. |GitHub-PRs| image:: https://img.shields.io/github/issues-pr-closed/tqdm/py-make.svg?logo=github&logoColor=white
   :target: https://github.com/tqdm/py-make/pulls
.. |GitHub-Contributions| image:: https://img.shields.io/github/contributors/tqdm/py-make.svg?logo=github&logoColor=white
   :target: https://github.com/tqdm/py-make/graphs/contributors
.. |GitHub-Updated| image:: https://img.shields.io/github/last-commit/tqdm/py-make/master.svg?logo=github&logoColor=white&label=pushed
   :target: https://github.com/tqdm/py-make/pulse
.. |PyPI-Status| image:: https://img.shields.io/pypi/v/py-make.svg
   :target: https://pypi.org/project/py-make
.. |PyPI-Downloads| image:: https://img.shields.io/pypi/dm/py-make.svg?label=pypi%20downloads&logo=python&logoColor=white
   :target: https://pypi.org/project/py-make
.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/py-make.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/py-make
.. |Libraries-Rank| image:: https://img.shields.io/librariesio/sourcerank/pypi/py-make.svg?logo=koding&logoColor=white
   :target: https://libraries.io/pypi/py-make
.. |Libraries-Dependents| image:: https://img.shields.io/librariesio/dependent-repos/pypi/py-make.svg?logo=koding&logoColor=white
    :target: https://github.com/tqdm/py-make/network/dependents
.. |OpenHub-Status| image:: https://www.openhub.net/p/tqdm_py-make/widgets/project_thin_badge?format=gif
   :target: https://www.openhub.net/p/tqdm_py-make?ref=Thin+badge
.. |LICENCE| image:: https://img.shields.io/pypi/l/py-make.svg
   :target: https://raw.githubusercontent.com/tqdm/py-make/master/LICENCE
.. |DOI-URI| image:: https://img.shields.io/badge/DOI-10.5281/zenodo.2546871-blue.svg
   :target: https://doi.org/10.5281/zenodo.2546871
.. |README-Hits| image:: https://caspersci.uk.to/cgi-bin/hits.cgi?q=py-make&style=social&r=https://github.com/tqdm/py-make
   :target: https://caspersci.uk.to/cgi-bin/hits.cgi?q=py-make&a=plot&r=https://github.com/tqdm/py-make&style=social
