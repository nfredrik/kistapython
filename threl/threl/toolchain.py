# -*- coding: utf-8 -*-

"""Specifies the different toolchain settings.

The following toolchains are available:

  iglx -- Compulab iGLX
  ppc603 -- Freescale MPC5121

All of the toolchains specify the following settings:

  cxxflags -- C++ compiler flags
  libdir -- Directory name where the libs for this environment is
  package -- Class that builds packages for this specific toolchain
  toolchain -- Name of the toolchain
"""

import package

iglx = {'arch': 'i386',
        'cxxflags': '-Wno-long-long -Os',
        'libdir': '/opt/env/iglx',
        'package': package.TarBz2Package,
        'toolchain': 'gcc-4.2.0-glibc-2.5/i686-unknown-linux-gnu'}
ppc603 = {'arch': 'powerpc',
          'cxxflags': '-Wno-long-long -O2',
          'libdir': '/opt/env/lenny-ppc',
          'package': package.DebPackage,
          'toolchain': 'gcc-4.2.0-glibc-2.5/powerpc-603-linux-gnu'}
toolchain = {'iglx': iglx, 'ppc603': ppc603}

__all__ = ['toolchain']
