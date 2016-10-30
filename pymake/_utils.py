import sys

__all__ = ["ConfigParser", "StringIO", "_sh", "shlex"]

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

if sys.version_info >= (2, 7):  # pragma: no cover
    import shlex
else:  # pragma: no cover
    import re

    class shlex(object):
        """ Emulate built-in shlex.split using re """
        # tokens may be surrounded by unescaped quote pairs
        RE_TOKEN = re.compile(r'(?<!\\)(?P<q>[\'"])(.*?)(?<!\\)(?P=q)')
        RE_WTSPC = re.compile(r'\s+')
        # unescaped hash (designates a comment when unquoted)
        RE_CMMNT = re.compile(r'(.*?)(?<!\\)#')

        @classmethod
        def split(cls, cmd, comments=True):
            toks = cls.RE_TOKEN.split(cmd)
            res = []
            quoted = False
            for t in toks:
                if quoted:
                    if t:
                        res.append(t)
                    quoted = False
                elif t in '\'"':
                    quoted = True
                elif t:
                    c = cls.RE_CMMNT.split(t)
                    uncom = (c[0] or c[1]).strip()
                    if uncom:
                        res.extend(cls.RE_WTSPC.split(uncom))
                    if len(c) > 1:
                        break  # rest is comment
            return res


def _sh(*cmd, **kwargs):
    import subprocess
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            **kwargs).communicate()[0].decode('utf-8')
