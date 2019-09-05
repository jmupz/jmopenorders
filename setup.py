#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2019 Jürgen Mülbert. All rights reserved.
#
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
#
# Lizenziert unter der EUPL, Version 1.2 oder - sobald
#  diese von der Europäischen Kommission genehmigt wurden -
# Folgeversionen der EUPL ("Lizenz");
# Sie dürfen dieses Werk ausschließlich gemäß
# dieser Lizenz nutzen.
# Eine Kopie der Lizenz finden Sie hier:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Sofern nicht durch anwendbare Rechtsvorschriften
# gefordert oder in schriftlicher Form vereinbart, wird
# die unter der Lizenz verbreitete Software "so wie sie
# ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
# ausdrücklich oder stillschweigend - verbreitet.
# Die sprachspezifischen Genehmigungen und Beschränkungen
# unter der Lizenz sind dem Lizenztext zu entnehmen.
#

"""The setup.py file for Python openorders."""

from setuptools import setup, find_packages
import pkg_resources
import sys
import os

__version__ = '0.1.0'

try:
    if int(pkg_resources.get_distribution("pip").version.split('.')[0]) < 6:
        print('pip older than 6.0 not supported, please upgrade pip with:\n\n'
              '    pip install -U pip')
        sys.exit(-1)
except pkg_resources.DistributionNotFound:
    pass

if os.environ.get('CONVERT_README'):
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
else:
    long_description = ''

version = sys.version_info[:2]
if version < (2, 7):
    print('jmopenorders requires Python version 2.7 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)
elif (3, 0) < version < (3, 4):
    print('jmopenorders requires Python version 3.4 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)



install_requires = ['psutil', 'colorama', 'six', 'decorator', 'pyte']
extras_require = {':python_version<"3.4"': ['pathlib2'],
                  ':python_version<"3.3"': ['backports.shutil_get_terminal_size'],
                  ":sys_platform=='win32'": ['win_unicode_console']}

setup(
    name='jmopenorders',
    version=__version__,
    # Authorship and online reference
    author='Jürgen Mülbert',
    author_email='juergen.muelbert@gmail.com',
    url='https://github.com/jmuelbert/jmopenorders',
    # Detailled description
    description='Create OpenOrders Reports',
    long_description='Create Excel Reports from the OpenOrders File from CarLO',
    long_description_content_type='text/markdown',
    keywords='business report',
    download_url='https://github.com/jmuelbert/jmopenorders/tarball' + __version__,
    license="EUPL-1.2",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",

        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],
    # Package configuration
    packages=find_packages(exclude=('ez_setup', 'examples',
                                    'tests', 'tests.*',
                                    'release', 'docs')),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=install_requires,
    dependeny_links=dependency_links,
    entry_points={
        'console_scripts': [
            'jmopenorders = jmopenorders.entrypoints.main:main',
            'jmorders = jmopenorders.entrypoints.not_configured:main'
        ]
    }
)
