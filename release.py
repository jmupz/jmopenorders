#!/usr/bin/env python
# encoding: utf-8

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

from subprocess import call
import os
import re

version = None


def get_new_setup_py_lines():
    global version
    with open('setup.py', 'r') as sf:
        current_setup = sf.readlines()
    for line in current_setup:
        if line.startswith('VERSION = '):
            major, minor = re.findall(r"VERSION = '(\d+)\.(\d+)'", line)[0]
            version = "{}.{}".format(major, int(minor) + 1)
            yield "VERSION = '{}'\n".format(version)
        else:
            yield line


lines = list(get_new_setup_py_lines())
with open('setup.py', 'w') as sf:
    sf.writelines(lines)

call('git pull', shell=True)
call('git commit -am "Bump to {}"'.format(version), shell=True)
call('git tag {}'.format(version), shell=True)
call('git push', shell=True)
call('git push --tags', shell=True)

env = os.environ
env['CONVERT_README'] = 'true'
call('rm -rf dist/*')
call('python setup.py sdist bdist_wheel', shell=True, env=env)
call('twine upload dist/*', shell=True, env=env)
