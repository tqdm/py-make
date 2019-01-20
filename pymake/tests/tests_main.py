import sys
import subprocess
from os import path
from textwrap import dedent
from pymake import main, PymakeKeyError, PymakeTypeError

dn = path.dirname
fname = path.join(dn(dn(dn(path.abspath(__file__)))),
                  "examples", "Makefile").replace('\\', '/')


def _sh(*cmd, **kwargs):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            **kwargs).communicate()[0].decode('utf-8')


def test_main():
    """Test execution"""
    res = _sh(sys.executable, '-c', dedent('''\
              from pymake import main; import sys
              sys.argv = ["", "-f", "''' + fname + '''"]
              main()
              '''),
              stderr=subprocess.STDOUT)

    # actual test:
    assert ("hello world" in res)

    # semi-fake test which gets coverage:
    _SYS = sys.argv
    sys.argv = ['', '-f', fname]
    main()
    sys.argv = _SYS


def test_invalid_alias():
    """Test invalid alias"""
    _SYS = sys.argv
    sys.argv = ['', '-f', fname, 'foo']
    try:
        main()
    except PymakeKeyError as e:
        if 'foo' not in str(e):
            raise
    else:
        raise PymakeKeyError('foo')
    sys.argv = _SYS


def test_multi_target():
    """Test various targets"""
    _SYS = sys.argv
    for trg in ['circle', 'empty', 'one']:
        sys.argv = ['', '-s', '-f', fname, trg]
        main()
    sys.argv = _SYS


def test_print_data_base():
    """Test --print-data-base with errors"""
    _SYS = sys.argv
    sys.argv = ['', '-s', '-p', '-f', fname, 'err']
    main()
    sys.argv = _SYS


def test_just_print():
    """Test --just-print with errors"""
    _SYS = sys.argv
    sys.argv = ['', '-s', '-n', '-f', fname, 'err']
    main()
    sys.argv = _SYS


def test_ignore_errors():
    """Test --ignore-errors"""
    _SYS = sys.argv
    sys.argv = ['', '-s', '-f', fname, 'err']
    try:
        main()
    except OSError:
        pass  # test passed if file not found
    else:
        raise PymakeTypeError('err')

    sys.argv = ['', '-s', '-i', '-f', fname, 'err']
    main()
    sys.argv = _SYS


def test_help_version():
    """Test help and version"""
    _SYS = sys.argv
    for i in ('-h', '--help', '-v', '--version'):
        sys.argv = ['', i]
        try:
            main()
        except SystemExit:
            pass
    sys.argv = _SYS
