# IMPORTANT: for compatibility with `python setup.py make [alias]`, ensure:
# 1. Every alias is preceded by @[+]make (eg: @make alias)
# 2. A maximum of one @make alias or command per line
# see: https://github.com/tqdm/py-make/issues/1

.PHONY:
	alltests
	all
	flake8
	test
	pytest
	testsetup
	testcoverage
	testtimer
	distclean
	coverclean
	prebuildclean
	clean
	toxclean
	install_dev
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
	@+flake8 -j 8 --count --statistics --exit-zero .

test:
	tox --skip-missing-interpreters

pytest:
	pytest

testsetup:
	@make help

testcoverage:
	@make coverclean
	pytest --cov=pymake --cov-report=xml --cov-report=term --cov-fail-under=80

testtimer:
	pytest

distclean:
	@+make coverclean
	@+make prebuildclean
	@+make clean
prebuildclean:
	@+python -c "import shutil; shutil.rmtree('build', True)"
	@+python -c "import shutil; shutil.rmtree('dist', True)"
	@+python -c "import shutil; shutil.rmtree('pymake.egg-info', True)"
	@+python -c "import shutil; shutil.rmtree('.eggs', True)"
coverclean:
	@+python -c "import os; os.remove('.coverage') if os.path.exists('.coverage') else None"
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('.coverage.*')]"
	@+python -c "import shutil; shutil.rmtree('tests/__pycache__', True)"
	@+python -c "import shutil; shutil.rmtree('pymake/__pycache__', True)"
	@+python -c "import shutil; shutil.rmtree('examples/__pycache__', True)"
clean:
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('*.py[co]')]"
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('tests/*.py[co]')]"
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('pymake/*.py[co]')]"
	@+python -c "import os, glob; [os.remove(i) for i in glob.glob('examples/*.py[co]')]"
toxclean:
	@+python -c "import shutil; shutil.rmtree('.tox', True)"


install:
	python -m pip install .
install_dev:
	python -m pip install -e .

build:
	@make prebuildclean
	@make testsetup
	python -m build
	python -m twine check dist/*

pypi:
	python -m twine upload dist/*

buildupload:
	@make build
	@make pypi

none:
	# used for unit testing

run:
	python -Om pymake
