# -*- coding: utf-8 -*-

from optparse import OptionGroup, OptionParser
import sys

from project import autodetect_project
from version import version


class Logger:
    """Logger class with automatic verbosity checking"""

    def __init__(self, verbose):
        self.__verbose = verbose

    def __call__(self, level, msg):
        if level <= self.__verbose:
            print msg


def generate_parser():
    """Generate a command line option parser"""

    description = 'Create a release package with the specified version. '\
                  'This script will automagically figure out what project '\
                  'you want to build, the revision control system used and '\
                  'stuff like that.'
    usage = 'usage: %prog [options] version'
    parser = OptionParser(description=description, usage=usage,
                          version='%prog ' + version)
    parser.set_defaults(verbose=0)
    parser.add_option('-r', '--revision', metavar='REVISION',
                      help='build release from REVISION')
    parser.add_option('-v', '--verbose',
                      action='count', dest='verbose',
                      help='enable additional output, specify several times '\
                           'for more information')

    # Create a group for the platform where this application is meant to run
    group = OptionGroup(parser, 'Platform options')
    group.add_option('--i686',
                     action='store_const', dest='platform', const='i686',
                     help='Compulab i686')
    group.add_option('--iglx',
                     action='store_const', dest='platform', const='iglx',
                     help='Compulab iGLX (AMD K6-2)')
    group.add_option('--ppc603',
                     action='store_const', dest='platform', const='ppc603',
                     help='PowerPC 603 (Freescale MPC5121)')
    parser.add_option_group(group)

    return parser


def main():
    # Parse command line arguments and do basic sanity checks
    parser = generate_parser()
    (options, args) = parser.parse_args()
    if options.platform == None:
        parser.error('No platform defined (see "threl --help")')
    if len(args) < 1:
        parser.error('No version defined (see "threl --help")')

    # Detect the project
    log = Logger(options.verbose)
    project = autodetect_project(log, options.platform)
    if project == None:
        print 'No project found'
        sys.exit(1)

    project.build(log, options.platform)
    project.package(log, args[0])
    project.cleanup(log)
