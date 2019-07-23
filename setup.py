#!python
# -*- coding: utf-8 -*-
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys
from io import open as io_open

# Get version from pymake/_version.py
__version__ = None
src_dir = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(src_dir, 'pymake', '_version.py')
with io_open(version_file, mode='r') as fd:
    exec(fd.read())

# Executing makefile commands if specified
if sys.argv[1].lower().strip() == 'make':
    import pymake  # requires package to be installed already
    # Filename of the makefile
    fpath = os.path.join(src_dir, 'Makefile')
    pymake.main(['-f', fpath] + sys.argv[2:])
    # Stop to avoid setup.py raising non-standard command error
    sys.exit(0)

README_rst = ''
fndoc = os.path.join(src_dir, 'README.rst')
with io_open(fndoc, mode='r', encoding='utf-8') as fd:
    README_rst = fd.read()

setup(
    name='py-make',
    version=__version__,
    description='Makefile execution powered by pure Python',
    long_description=README_rst,
    license='MPLv2.0, MIT Licenses',
    author='Casper da Costa-Luis',
    author_email='casper.dcl@physics.org',
    url='https://github.com/tqdm/pymake',
    maintainer='tqdm developers',
    maintainer_email='python.tqdm@gmail.com',
    platforms=['any'],
    packages=['pymake'],
    install_requires=['docopt>=0.6.0', 'six'],
    entry_points={'console_scripts': ['pymake=pymake._main:main'], },
    package_data={'py-make': ['CONTRIBUTE', 'LICENCE',
                              'examples/*.py', 'examples/Makefile*']},
    python_requires='>=2.6, !=3.0.*, !=3.1.*',
    classifiers=[
        # Trove classifiers
        # (https://pypi.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Other Environment',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Desktop Environment',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: Education :: Testing',
        'Topic :: Office/Business',
        'Topic :: Other/Nonlisted Topic',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Shells',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
    keywords='make makefile gnumake gnu console terminal cli',
    test_suite='nose.collector',
    tests_require=['nose', 'flake8', 'coverage'],
)
