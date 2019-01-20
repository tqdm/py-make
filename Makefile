# IMPORTANT: for compatibility with `python setup.py make [alias]`, ensure:
# 1. Every alias is preceded by @[+]make (eg: @make alias)
# 2. A maximum of one @make alias or command per line
# see: https://github.com/tqdm/py-make/issues/1

.PHONY:
	alltests
	all
	flake8
	test
	testnose
	testsetup
	testcoverage
	testtimer
	distclean
	coverclean
	prebuildclean
	clean
	toxclean
	installdev
	install
	build
	buildupload
	pypi
	help
	none
	run

help:
	@python setup.py make -p

alltests:
	@+make testcoverage
	@+make flake8
	@+make testsetup

all:
	@+make alltests
	@+make build

flake8:
	@+flake8 --max-line-length=80 --exclude .tox,build \
    -j 8 --count --statistics --exit-zero .

test:
	tox --skip-missing-interpreters

testnose:
	nosetests pymake -d -v

testsetup:
	python setup.py check --restructuredtext --strict
	python setup.py make none

testcoverage:
	@make coverclean
	nosetests pymake --with-coverage --cover-package=pymake --cover-erase --cover-min-percentage=80 -d -v

testtimer:
	nosetests pymake --with-timer -d -v

distclean:
	@+make coverclean
	@+make prebuildclean
	@+make clean
prebuildclean:
	@+python -c "import shutil; shutil.rmtree('build', True)"
	@+python -c "import shutil; shutil.rmtree('dist', True)"
	@+python -c "import shutil; shutil.rmtree('pymake.egg-info', True)"
coverclean:
	@+python -c "import os; os.remove('.coverage') if os.path.exists('.coverage') else None"
	@+python -c "import shutil; shutil.rmtree('pymake/__pycache__', True)"
	@+python -c "import shutil; shutil.rmtree('pymake/tests/__pycache__', True)"
clean:
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('*.py[co]')]"
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('pymake/*.py[co]')]"
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('pymake/tests/*.py[co]')]"
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('pymake/examples/*.py[co]')]"
toxclean:
	@+python -c "import shutil; shutil.rmtree('.tox', True)"


installdev:
	python setup.py develop --uninstall
	python setup.py develop

install:
	python setup.py install

build:
	@make prebuildclean
	python setup.py sdist bdist_wheel
	# python setup.py bdist_wininst

pypi:
	twine upload dist/*

buildupload:
	@make testsetup
	@make build
	@make pypi

none:
	# used for unit testing

run:
	python -Om pymake
