#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name = 'threl',
    version = 'development',
    description = 'Release utility for Linux-based Thoreb software',
    long_description = '''\
Build and release script for Thoreb vehicle computers. Handles most of the
tricky business that's required when cross-compiling.''',
    author = 'Jens Bäckman',
    author_email = 'jens@titv,se',
    packages = find_packages(),
    entry_points = {
        'console_scripts': ['threl = threl.cli:main']
    },
    zip_safe = True
)
