import sys
import subprocess
from pathlib import Path
from pymake import main, PymakeKeyError, PymakeTypeError

fname = str(Path(__file__).parent.parent.resolve() / "examples" / "Makefile")


def _sh(*cmd, **kwargs):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            **kwargs).communicate()[0].decode('utf-8')


def test_main():
    """Test execution"""
    res = _sh(sys.executable, '-c', ('\
              import pymake; pymake.main(["-f", "%s"])' % fname).strip(),
              stderr=subprocess.STDOUT)

    # actual test:
    assert "hello world" in res

    # semi-fake test which gets coverage:
    _SYS = sys.argv
    sys.argv = ['', '-f', fname]
    main()
    sys.argv = _SYS


def test_invalid_alias():
    """Test invalid alias"""
    try:
        main(['-f', fname, 'foo'])
    except PymakeKeyError as e:
        if 'foo' not in str(e):
            raise
    else:
        raise PymakeKeyError('foo')


def test_multi_target():
    """Test various targets"""
    for trg in ['circle', 'empty', 'one']:
        main(['-s', '-f', fname, trg])


def test_print_data_base():
    """Test --print-data-base with errors"""
    main(['-s', '-p', '-f', fname, 'err'])


def test_just_print():
    """Test --just-print with errors"""
    main(['-s', '-n', '-f', fname, 'err'])


def test_ignore_errors():
    """Test --ignore-errors"""
    try:
        main(['-s', '-f', fname, 'err'])
    except OSError:
        pass  # test passed if file not found
    else:
        raise PymakeTypeError('err')

    main(['-s', '-i', '-f', fname, 'err'])


def test_help_version():
    """Test help and version"""
    for i in ('-h', '--help', '-v', '--version'):
        try:
            main([i])
        except SystemExit:
            pass
