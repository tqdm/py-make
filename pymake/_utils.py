__all__ = ["ConfigParser", "StringIO", "_sh"]

if True:  # pragma: no cover
    try:
        import ConfigParser
        import StringIO
    except ImportError:
        import configparser as ConfigParser
        import io as StringIO

    try:
        _unich = unichr
    except NameError:
        _unich = chr

    try:
        _unicode = unicode
    except NameError:
        _unicode = str


def _sh(*cmd, **kwargs):
    import subprocess
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            **kwargs).communicate()[0].decode('utf-8')
