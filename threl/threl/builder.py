# -*- coding: utf-8 -*-

import os
import tempfile

from toolchain import toolchain


class Builder(object):
    builddir = tempfile.mkdtemp()
    _processors = 0

    def __init__(self):
        for line in open('/proc/cpuinfo', 'r'):
            if line.startswith('processor'):
                self._processors += 1

    def build(self, log, target=''):
        log(1, 'Building using %d processors' % self._processors)
        cmd = 'cd %s;make -j%d %s' % (self.builddir, self._processors, target)
        if os.system(cmd):
            raise Exception('Error when building')

    def cleanup(self, log):
        log(2, 'Removing temporary directory %s' % self.builddir)
        os.system('rm -rf %s' % self.builddir)


class CMakeBuilder(Builder):
    """CMake project builder"""

    def _fix_link(self, filename, platform):
        file = open(filename, 'r')
        line = file.readline().split()
        file.close()

        libdir = toolchain[platform]['libdir']
        line.insert(1, '-L%s/usr/lib' % libdir)
        line.insert(2, '-L%s/lib' % libdir)
        line.insert(3, '-Wl,-rpath-link,%s/usr/lib' % libdir)
        line.insert(4, '-Wl,-rpath-link,%s/lib' % libdir)

        file = open(filename, 'w')
        file.write(' '.join(line))
        file.close()

    def fix_link(self, log, target, platform):
        log(1, 'Fixing linkage for %s' % target)
        targetdir = '%s.dir' % target
        for root, dirs, files in os.walk(self.builddir):
            if 'link.txt' in files:
                head, tail = os.path.split(root)
                if tail == targetdir:
                    log(2, 'Found link file in %s' % root)
                    self._fix_link(os.path.join(root, 'link.txt'), platform)

    def prepare(self, log, directory, platform):
        log(1, 'Compiling for %s' % platform)
        platform = toolchain[platform]

        # Get the correct toolchain file for CMake
        cross = platform['toolchain']
        cross = os.path.join('/opt/crosstool', cross)
        cross = os.path.join(cross, 'toolchain.cmake')
        cross = '-DCMAKE_TOOLCHAIN_FILE=' + cross

        # Setup CMake
        log(2, 'Preparing build environment')
        cxxflags = '-I%s/usr/include %s' % (platform['libdir'],
                                            platform['cxxflags'])
        cmd = 'cd %s; CXXFLAGS="%s" cmake -DHAS_PNG=1 -DHAS_IGLX=0 -DHAS_I686=0 %s %s'
        cmd %= (self.builddir, cxxflags, cross, directory)
        if os.system(cmd):
            raise Exception('Error when preparing the build environment')


class QMakeBuilder(Builder):
    """QMake project builder"""

    def __init__(self, filename):
        self.filename = filename
        super(QMakeBuilder, self).__init__()

    def prepare(self, log, directory, platform):
        log(1, 'Compiling for %s' % platform)
        platform = toolchain[platform]

        # Setup qmake
        log(2, 'Preparing build environment')
        cxxflags = platform['cxxflags']
        spec = platform['libdir']
        cmd = 'cd %s; CXXFLAGS="%s" qmake "DEFINES += HAS_SMOKE" -spec %s %s/%s'
        cmd %= (self.builddir, cxxflags, spec, directory, self.filename)
        if os.system(cmd):
            raise Exception('Error when preparing the build environment')
