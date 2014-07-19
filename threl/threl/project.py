# -*- coding: utf-8 -*-

import os
import shutil
import string
import tempfile

from toolchain import toolchain
import builder
import package


class Project:
    """Base class for all projects"""

    def __init__(self, directory, platform):
        self._directory = directory
        self._toolchain = toolchain[platform]
        self._package = self._toolchain['package']()

    def _copydir_without_svn(self, src, dest):
        try:
            os.makedirs(dest)
        except OSError:
            pass

        for root, dirs, files in os.walk(src):
            if '.svn' in dirs:
                dirs.remove('.svn')
            destpath = dest + root.replace(src, '') + '/'
            for dir in dirs:
                os.mkdir(destpath + dir)
            for file in files:
                shutil.copy(root + '/' + file, destpath + file)

    def build(self, log, platform):
        raise NotImplementedError

    def cleanup(self, log):
        raise NotImplementedError

    def package(self, log):
        raise NotImplementedError


class AppLauncher(Project):
    current_project_file = 'src/AppLauncher.cpp'
    deps_deb = 'smoke-0.6, libqtgui4'
    name = 'AppLauncher'
    __builder = builder.QMakeBuilder('applauncher.pro')

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        os.makedirs('%s/usr/bin' % packdir)
        cmd = 'cd %s;cp applauncher %s/usr/bin'
        os.system(cmd % (self.__builder.builddir, packdir))
        self._package.create(log, 'applauncher', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class Barcode(Project):
    current_project_file = 'barcode.pro'
    deps_deb = 'libqtgui4, smoke-0.4'
    name = 'Barcode'
    __builder = builder.QMakeBuilder('barcode.pro')

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        os.makedirs('%s/usr/bin' % packdir)
        cmd = 'cd %s;cp barcode %s/usr/bin'
        os.system(cmd % (self.__builder.builddir, packdir))
        self._package.create(log, 'barcode', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class BigSister(Project):
    current_project_file = 'src/bigsister.cpp'
    deps_deb = 'bzip2, libsdl-gfx1.2-4, libsvg-1.6, mplayer, ppp, rsync, smoke-0.4'
    name = 'Big Sister'
    __builder = builder.CMakeBuilder()

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.fix_link(log, 'bigsister', platform)
        self.__builder.fix_link(log, 'slavesign', platform)
        os.system('ln -s %s/.hg %s/' % (self._directory, self.__builder.builddir))
        self.__builder.build(log, 'bigsister')
        self.__builder.build(log, 'slavesign')

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        log(2, 'Copying bigsister')
        os.makedirs(packdir + '/usr/bin')
        shutil.copy(self.__builder.builddir + '/bigsister',
                    packdir + '/usr/bin')
        shutil.copy(self.__builder.builddir + '/slavesign',
                    packdir + '/usr/bin')

        log(2, 'Copying data files')
        self._copydir_without_svn(self._directory + '/data_bigsister',
                                  packdir + '/root/bigsister')
        os.system('rm -rf %s/root/bigsister/configuration_set' % packdir)
        self._copydir_without_svn(self._directory + '/data_slavesign',
                                  packdir + '/root/slavesign')
        self._copydir_without_svn(self._directory + '/platform/mpc5121',
                                  packdir + '/root/bigsister')
        os.system('cd %s/root/slavesign; ln -s /mnt/writable/data/traffic_set/default traffic' % packdir)
        self._package.create(log, 'driverinterface', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class CanServer(Project):
    current_project_file = 'src/CanServer.cpp'
    deps_deb = 'smoke-0.6'
    name = 'CanServer'
    __builder = builder.CMakeBuilder()

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.fix_link(log, 'canserver', platform)
        self.__builder.build(log, 'canserver')

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        log(2, 'Copying canserver')
        os.makedirs(packdir + '/usr/bin')
        shutil.copy(self.__builder.builddir + '/canserver',
                    packdir + '/usr/bin')

        self._package.create(log, 'canserver', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)

class Clog(Project):
    current_project_file = 'clog.pro'
    deps_deb = 'libqtgui4, smoke-0.4'
    name = 'Clog'
    __builder = builder.QMakeBuilder('clog.pro')

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        os.makedirs('%s/usr/bin' % packdir)
        cmd = 'cd %s;cp clog %s/usr/bin'
        os.system(cmd % (self.__builder.builddir, packdir))
        self._package.create(log, 'clog', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class Ecco(Project):
    current_project_file = 'ecco/xp.h'
    deps_deb = 'libsqlite3-0, libxml2'
    name = 'Ecco'
    __builder = builder.CMakeBuilder()

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.fix_link(log, 'ecco-1.10', platform)
        self.__builder.fix_link(log, 'ecco-1.11', platform)
        self.__builder.fix_link(log, 'ecco-1.12', platform)
        self.__builder.fix_link(log, 'ecco-sqlite-1.10', platform)
        self.__builder.fix_link(log, 'ecco-sqlite-1.11', platform)
        self.__builder.fix_link(log, 'ecco-sqlite-1.12', platform)
        self.__builder.fix_link(log, 'ecco-xml-1.10', platform)
        self.__builder.fix_link(log, 'ecco-xml-1.11', platform)
        self.__builder.fix_link(log, 'ecco-xml-1.12', platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        name = 'ecco-%s' % version[0:string.rfind(version, '.')]

        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()
        cmd = 'cd %s;make install DESTDIR=%s'
        cmd = cmd % (self.__builder.builddir, packdir)
        os.system(cmd)
        self._package.create(log, name, version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class LibElsyService(Project):
    current_project_file = 'elsyservice/ElsyCanService.h'
    deps_deb = 'ecco-1.12 (>= 1.12.0)'
    name = 'LibElsyService'
    __builder = builder.CMakeBuilder()

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.fix_link(log, 'elsyservice-0.6', platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        name = 'libelsyservice-%s' % version[0:string.rfind(version, '.')]

        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()
        cmd = 'cd %s;make install DESTDIR=%s'
        cmd = cmd % (self.__builder.builddir, packdir)
        os.system(cmd)
        self._package.create(log, name, version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)

class LibSVG(Project):
    current_project_file = 'libsvg/Document.h'
    deps_deb = 'ecco-1.10 (>= 1.10.0), libsdl-image1.2'
    name = 'LibSVG'
    __builder = builder.CMakeBuilder()

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.fix_link(log, 'svg-1.6', platform)
        self.__builder.fix_link(log, 'svg-1.8', platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        name = 'libsvg-%s' % version[0:string.rfind(version, '.')]

        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()
        cmd = 'cd %s;make install DESTDIR=%s'
        cmd = cmd % (self.__builder.builddir, packdir)
        os.system(cmd)
        self._package.create(log, name, version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class Moviebox(Project):
    current_project_file = 'moviebox.pro'
    deps_deb = 'ecco-1.10, libqt4-dbus, liblog4cxx9c2a'
    name = 'Moviebox'
    __builder = builder.QMakeBuilder('moviebox.pro')

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        name = 'moviebox'

        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()
        cmd = 'cd %s;make install INSTALL_ROOT=%s'
        cmd = cmd % (self.__builder.builddir, packdir)
        os.system(cmd)
        self._package.create(log, name, version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class Smoke(Project):
    current_project_file = 'src/smoke/Hardware.h'
    deps_deb = 'ecco-1.12'
    name = 'Smoke'
    __builder = builder.CMakeBuilder()

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.fix_link(log, 'smoke-0.2', platform)
        self.__builder.fix_link(log, 'smoke-0.3', platform)
        self.__builder.fix_link(log, 'smoke-0.4', platform)
        self.__builder.fix_link(log, 'smoke-0.5', platform)
        self.__builder.fix_link(log, 'smoke-0.6', platform)
        self.__builder.fix_link(log, 'smoke-0.7', platform)
        self.__builder.fix_link(log, 'smoketool', platform)
        os.system('ln -s %s/.hg %s/' % (self._directory, self.__builder.builddir))
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        name = 'smoke-%s' % version[0:string.rfind(version, '.')]

        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        # Package the library
        cmd = 'cd %s;make install DESTDIR=%s;rm -rf %s/usr/bin'
        cmd = cmd % (self.__builder.builddir, packdir, packdir)
        os.system(cmd)
        self._package.create(log, name, version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)

        # Package smoketool
        cmd = 'rm -rf %s; mkdir -p %s/usr/bin; cp %s/smoketool %s/usr/bin/'
        cmd = cmd % (packdir, packdir, self.__builder.builddir, packdir)
        os.system(cmd)
        self._package.create(log, 'smoketool', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=name, replaces='smoke-0.1',
                             conflicts='smoke-0.1')


class TicketMachine(Project):
    current_project_file = 'src/TicketPanel.cpp'
    deps_deb = 'libqt4-gui, libqt4-sql-sqlite, libqt4-xml, smoke-0.4'
    name = 'Ticket Machine'
    __builder = builder.QMakeBuilder('ticketmachine.pro')

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        os.system('cd %s; make install INSTALL_ROOT=%s CHK_DIR_EXISTS="test -d" COPY="cp -f" MKDIR="mkdir -p"' %
                  (self.__builder.builddir, packdir))

        os.makedirs('%s/usr/bin' % packdir)
        cmd = 'cd %s;cp ticketmachine %s/usr/bin'
        os.system(cmd % (self.__builder.builddir, packdir))

        self._package.create(log, 'ticketmachine', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class Usbinstaller(Project):
    current_project_file = 'src/usbinstaller.cpp'
    deps_deb = 'ecco-1.10, libqt4-gui, psmisc, rsync'
    name = 'Usbinstaller'
    __builders = [builder.QMakeBuilder('usbinstaller.pro'),
                  builder.QMakeBuilder('usbwatcher.pro')]

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        for b in self.__builders:
            b.prepare(log, self._directory, platform)
            b.build(log)

    def cleanup(self, log):
        for b in self.__builders:
            b.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        os.makedirs('%s/etc/init.d' % packdir)
        cmd = 'cp %s/usbwatcher.init_debian %s/etc/init.d/usbwatcher'
        os.system(cmd % (self._directory, packdir))

        os.makedirs('%s/mnt/update' % packdir)
#        cmd = 'touch %s/mnt/update/.keep'
#        os.system(cmd % packdir)

        os.makedirs('%s/usr/bin' % packdir)
        cmd = 'cd %s;cp usbwatcher usbinstaller %s/usr/bin'
        for b in self.__builders:
            os.system(cmd % (b.builddir, packdir))

        cmd = 'cd %s;cp slax/install_data.sh %s/usr/bin'
        os.system(cmd % (self._directory, packdir))

        self._package.create(log, 'usbinstaller', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)


class Vixen(Project):
    current_project_file = 'src/Vixen.cpp'
    deps_deb = 'libelsyservice-0.6, libqt4-gui, libqt4-xml, mplayer, ppp, smoke-0.6, ttf-mscorefonts-installer'
    name = 'Vixen'
    __builder = builder.QMakeBuilder('vixen.pro')

    def __init__(self, directory, platform):
        Project.__init__(self, directory, platform)

    def build(self, log, platform):
        self.__builder.prepare(log, self._directory, platform)
        self.__builder.build(log)

    def cleanup(self, log):
        self.__builder.cleanup(log)

    def package(self, log, version):
        log(2, 'Creating package directory')
        packdir = tempfile.mkdtemp()

        os.makedirs('%s/usr/bin' % packdir)
        cmd = 'cd %s;cp vixen %s/usr/bin'
        os.system(cmd % (self.__builder.builddir, packdir))

        self._package.create(log, 'vixen', version, packdir,
                             arch=self._toolchain['arch'],
                             deps_deb=self.deps_deb)

        # Build TITV data
        packdir = tempfile.mkdtemp()
        self._copydir_without_svn(self._directory + '/defaultdata',
                                  packdir + '/root/vixen')
        self._package.create(log, 'vixen-data-titv', version, packdir,
                             arch='all', deps_deb='vixen',
                             conflicts='vixen-data-thoreb',
                             replaces='vixen-data-thoreb')

        # Build Thoreb data
        packdir = tempfile.mkdtemp()
        self._copydir_without_svn(self._directory + '/defaultdata-thoreb',
                                  packdir + '/root/vixen')
        self._package.create(log, 'vixen-data-thoreb', version, packdir,
                             arch='all', deps_deb='vixen',
                             conflicts='vixen-data-titv',
                             replaces='vixen-data-titv')


def autodetect_project(log, platform):
    """Try to detect the current project"""
    for project in projects:
        log(1, 'Checking if %s is the current project' % project.name)
        directory = file_exists(log, project.current_project_file)
        if len(directory):
            return project(directory, platform)
    return None


def file_exists(log, name):
    """Check if a file exists in or above the current working directory"""
    directory = os.getcwd()
    ignored = 'something'
    while ignored:
        path_and_name = os.path.join(directory, name)
        if os.path.isfile(path_and_name):
            log(2, 'Found %s' % path_and_name)
            return directory
        log(2, 'Could not find %s' % path_and_name)
        (directory, ignored) = os.path.split(directory)
    return ''

projects = [AppLauncher, Barcode, BigSister, CanServer, Clog, Ecco,
            LibElsyService, LibSVG, Moviebox, Smoke, TicketMachine,
            Usbinstaller, Vixen]
