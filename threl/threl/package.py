# -*- coding: utf-8 -*-

import hashlib
import os


class Package:
    """Base class for all packages"""

    def _create_hardlinks(self, log, builddir):
        """Find all files with duplicate contents, replace with hardlinks"""
        log(1, 'Checking for duplicate files')
        haystack = {}
        duplicates = 0
        size = 0
        for root, dirs, files in os.walk(builddir):
            for filename in files:
                filename = root + '/' + filename

                # Just make sure that this isn't a bloody symlink
                if os.path.islink(filename):
                    continue

                # Calculate the checksum
                check = hashlib.sha1()
                f = file(filename, 'rb')
                while True:
                    data = f.read(4096)
                    if len(data) == 0:
                        break
                    check.update(data)

                # See if this is already in the haystack
                needle = check.hexdigest()
                if needle in haystack:
                    duplicates += 1
                    size += os.stat(filename).st_size
                    os.remove(filename)
                    os.link(haystack[needle], filename)
                else:
                    haystack[needle] = filename

        log(1, '%d hardlinks created, %d bytes saved' % (duplicates, size))

    def create(self, log, name, version, builddir, **kwargs):
        raise NotImplementedError


class DebPackage(Package):
    """Debian package"""

    def create(self, log, name, version, builddir, **kwargs):
        self._create_hardlinks(log, builddir)

        arch = kwargs['arch']
        deps = kwargs['deps_deb']
        conflicts = kwargs.get('conflicts', '')
        replaces = kwargs.get('replaces', '')

        log(2, 'Creating Debian control file')
        os.makedirs(builddir + '/DEBIAN')
        control = open(builddir + '/DEBIAN/control', 'w')
        control.write('Package: %s\n' % name)
        control.write('Version: %s\n' % version)
        control.write('Architecture: %s\n' % arch)
        control.write('Maintainer: Thore Brynielsson <thore@thoreb.se>\n')
        control.write('Installed-Size: 12\n')
        control.write('Section: %s\n' % name)
        control.write('Depends: %s\n' % deps)
        control.write('Priority: extra\n')
        if conflicts != '':
            control.write('Conflicts: %s\n' % conflicts)
        if replaces != '':
            control.write('Replaces: %s\n' % replaces)
        control.write('Description: Thoreb package\n')
        control.close()

        log(1, 'Creating Debian package')
        cmd = 'dpkg-deb -Zlzma -b %s %s_%s_%s.deb'
        cmd %= (builddir, name, version, arch)
        os.system(cmd)


class TarBz2Package(Package):
    """Simple tar-bz2 package"""

    def create(self, log, name, version, builddir, **kwargs):
        self._create_hardlinks(log, builddir)
        log(2, 'Creating archive file')
        cmd = 'tar cfj %s-%s.tar.bz2 -C %s .' % (name, version, builddir)
        os.system(cmd)
