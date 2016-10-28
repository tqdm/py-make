# -*- coding: utf-8 -*-
"""Usage:
  pymake [--help | options] [<target>...]

Options:
  -h, --help     Print this help and exit
  -v, --version  Print version and exit
  -s, --silent   Don't echo commands (quiet)
  -p, --print-data-base  Print internal database
  -n, --just-print       Don't actually run any commands; just print them
                         (dry-run, recon)
  -i, --ignore-errors    Ignore errors from commands.
Arguments:
  -f FILE, --file FILE
                 Read FILE as a makefile (makefile) [default: Makefile]
"""
from __future__ import absolute_import
from __future__ import print_function
from ._pymake import parse_makefile_aliases, execute_makefile_commands, \
    PymakeKeyError
from ._version import __version__  # NOQA
from docopt import docopt
import sys


__all__ = ["main"]


def main():
    opts = docopt(__doc__, version=__version__)
    # Filename of the makefile
    fpath = opts['--file']

    # Parse the makefile, substitute the aliases and extract the commands
    commands, default_alias = parse_makefile_aliases(fpath)

    if opts['--print-data-base']:
        print("List of detected aliases:")
        print('\n'.join(alias for alias in sorted(commands.keys())))
        return

    if not opts['<target>']:
        opts['<target>'] = [default_alias]

    for target in opts['<target>']:
        if target in commands.keys():
            execute_makefile_commands(commands, target,
                                      silent=opts['--silent'],
                                      just_print=opts['--just-print'],
                                      ignore_errors=opts['--ignore-errors'])
        else:
            raise PymakeKeyError(sys.argv[0] +
                                 ": *** No rule to make target `" +
                                 target + "'. Stop.")
main.__doc__ = __doc__
