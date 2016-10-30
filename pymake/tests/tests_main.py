import sys
import subprocess
import os
from pymake import main, PymakeKeyError, PymakeTypeError


def _sh(*cmd, **kwargs):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            **kwargs).communicate()[0].decode('utf-8')


def repeat(fn, n, arg):
    a = arg
    for _ in range(n):
        a = fn(a)
    return a


# WARNING: this should be the last test as it messes with sys.stdin, argv
def test_main():
    """ Test execution """

    fname = os.path.join(os.path.abspath(repeat(os.path.dirname, 3, __file__)),
                         "examples", "Makefile").replace('\\', '/')
    res = _sh(sys.executable, '-c',
              'from pymake import main; import sys; ' +
              'sys.argv = ["", "-f", "' + fname + '"]; main()',
              stderr=subprocess.STDOUT)

    # actual test:
    assert ("hello world" in res)

    # semi-fake test which gets coverage:
    _SYS = sys.stdin, sys.argv

    sys.argv = ['', '-f', fname]
    main()

    """ Test invalid alias """
    sys.argv = ['', '-f', fname, 'foo']
    try:
        main()
    except PymakeKeyError as e:
        if 'foo' not in str(e):
            raise
    else:
        raise PymakeKeyError('foo')

    """ Test various targets """
    for trg in ['circle', 'empty', 'one']:
        sys.argv = ['', '-s', '-f', fname, trg]
        main()

    """ Test --print-data-base with errors """
    sys.argv = ['', '-s', '-p', '-f', fname, 'err']
    main()

    """ Test --just-print with errors """
    sys.argv = ['', '-s', '-n', '-f', fname, 'err']
    main()

    """ Test --ignore-errors """
    sys.argv = ['', '-s', '-f', fname, 'err']
    try:
        main()
    except OSError:
        pass  # test passed if file not found
    else:
        raise PymakeTypeError('err')

    sys.argv = ['', '-s', '-i', '-f', fname, 'err']
    main()

    """ Test help and version """
    for i in ('-h', '--help', '-v', '--version'):
        sys.argv = ['', i]
        try:
            main()
        except SystemExit:
            pass

    # clean up
    sys.stdin, sys.argv = _SYS
