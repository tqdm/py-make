"""
pymake helpers
"""
from __future__ import absolute_import
# import compatibility functions and utilities
from ._utils import ConfigParser, StringIO
import io
import re
from subprocess import check_call
import shlex


__author__ = {"github.com/": ["casperdcl", "lrq3000"]}
__all__ = ['PymakeTypeError', 'PymakeKeyError',
           'parse_makefile_aliases', 'execute_makefile_commands']


RE_MAKE_CMD = re.compile('^\t(@\+?)(make)?', flags=re.M)
RE_MACRO_DEF = re.compile(r"^(\S+)\s*\:?\=\s*(.*?)$", flags=re.M)
RE_MACRO = re.compile(r"\$\(\s*\S+\s*\)", flags=re.M)


class PymakeTypeError(TypeError):
    pass


class PymakeKeyError(KeyError):
    pass


def parse_makefile_aliases(filepath):
    '''
    Parse a makefile to find commands and substitute variables. Expects a
    makefile with only aliases and a line return between each command.

    Returns
    -------
    commands  : dict
        Maps each alias to a list of commands.
    default_alias  : str
    '''

    # -- Parsing the Makefile using ConfigParser
    # Adding a fake section to make the Makefile a valid Ini file
    ini_str = '[root]\n'
    with io.open(filepath, mode='r') as fd:
        ini_str = ini_str + RE_MAKE_CMD.sub('\t', fd.read())

    # Substitute macros
    macros = dict(RE_MACRO_DEF.findall(ini_str))
    for _ in range(99):  # allow finite amount of nesting
        for (m, expr) in macros.items():
            remacros = re.compile(r"\$\(" + m + "\)", flags=re.M)
            ini_str = remacros.sub(expr, ini_str)
        if not RE_MACRO.match(ini_str):
            # Remove macro definitions from rest of parsing
            ini_str = RE_MACRO_DEF.sub("", ini_str)
            break
    else:
        raise PymakeKeyError("No substitution for macros: " +
                             str(set(RE_MACRO.findall(ini_str))))

    ini_fp = StringIO.StringIO(ini_str)
    # Parse using ConfigParser
    config = ConfigParser.RawConfigParser()
    config.readfp(ini_fp)
    # Fetch the list of aliases
    aliases = config.options('root')

    # -- Extracting commands for each alias
    commands = {}
    default_alias = ''
    for alias in aliases:
        if alias.lower() in ['.phony']:
            continue
        if not default_alias:
            default_alias = alias
        # strip the first line return, and then split by any line return
        commands[alias] = config.get('root', alias).lstrip('\n').split('\n')

    # -- Commands substitution
    # Loop until all aliases are substituted by their commands:
    # Check each command of each alias, and if there is one command that is to
    # be substituted by an alias, try to do it right away. If this is not
    # possible because this alias itself points to other aliases , then stop
    # and put the current alias back in the queue to be processed again later.

    # Create the queue of aliases to process
    aliases_todo = list(commands.keys())
    # Create the dict that will hold the full commands
    commands_new = {}
    # Loop until we have processed all aliases
    while aliases_todo:
        # Pick the first alias in the queue
        alias = aliases_todo.pop(0)
        # Create a new entry in the resulting dict
        commands_new[alias] = []
        # For each command of this alias
        for cmd in commands[alias]:
            # Ignore self-referencing (alias points to itself)
            if cmd == alias:
                pass
            # Substitute full command
            elif cmd in aliases and cmd in commands_new:
                # Append all the commands referenced by the alias
                commands_new[alias].extend(commands_new[cmd])
            # Delay substituting another alias, waiting for the other alias to
            # be substituted first
            elif cmd in aliases and cmd not in commands_new:
                # Delete the current entry to avoid other aliases
                # to reference this one wrongly (as it is empty)
                del commands_new[alias]
                aliases_todo.append(alias)
                break
            # Full command (no aliases)
            else:
                commands_new[alias].append(cmd)
    commands = commands_new
    del commands_new

    # -- Prepending prefix to avoid conflicts with standard setup.py commands
    # for alias in commands.keys():
    #     commands['make_'+alias] = commands[alias]
    #     del commands[alias]

    return commands, default_alias


def execute_makefile_commands(
        commands, alias, silent=False, just_print=False, ignore_errors=False):
    """
    Execution Handler

    Parameters
    ----------
    commands  : dict
        Maps each alias to a list of commands.
    alias  : str

    Bool Options (default-false)
    ----------------------------
    silent, just_print, ignore_errors
    """
    cmds = commands[alias]

    if just_print:
        print('\n'.join(cmds))
        return

    for cmd in cmds:
        # Parse string in a shell-like fashion
        # (incl quoted strings and comments)
        parsed_cmd = shlex.split(cmd, comments=True)
        # Execute command if not empty (ie, not just a comment)
        if parsed_cmd:
            if not silent:
                print(cmd)
            # Launch the command and wait to finish (synchronized call)
            try:
                check_call(parsed_cmd)
            except:
                if not ignore_errors:
                    raise
