import sys
import subprocess
import os
from pymake import main, PymakeKeyError


# def test_subprocess()
#     """Explicit alternative"""
#     import subprocess
#     subprocess.Popen("pymake",
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.STDOUT).communicate()[0].decode('utf-8')


def _sh(*cmd, **kwargs):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            **kwargs).communicate()[0].decode('utf-8')


def repeat(fn, n, *args):
    a = args
    for _ in range(n):
        a = fn(*a)
    return a


# WARNING: this should be the last test as it messes with sys.stdin, argv
def test_main():
    """ Test execution """

    fname = path.join(path.abspath(repeat(os.path.dirname, 3, __file__)),
                      "examples", "Makefile")
    res = _sh(sys.executable, '-c',
              'from pymake import main; import sys; '
              'sys.argv = ["", "-f", "{}"]'.format(fname)
              'main()',
              stderr=subprocess.STDOUT)

    # actual test:

    assert ("hello world" in res)

    # semi-fake test which gets coverage:
    try:
        _SYS = (deepcopy(sys.stdin), deepcopy(sys.argv))
    except:
        pass

    sys.argv = ['', '-f', fname]
    main()

    sys.argv = ['', '-f', fname, 'hel']
    try:
        main()
    except PymakeKeyError as e:
        if 'foo' not in str(e):
            raise
    else:
        raise PymakeKeyError('foo')

    sys.argv = ['', '-s', '-f', fname, 'hel']
    main()

    for i in ('-h', '--help', '-v', '--version'):
        sys.argv = ['', i]
        try:
            main()
        except SystemExit:
            pass

    # clean up
    try:
        sys.stdin, sys.argv = _SYS
    except:
        pass
