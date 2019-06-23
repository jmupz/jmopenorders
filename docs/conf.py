# -*- coding: utf-8 -*-

import sys
import re
from os.path import abspath, join, dirname
from datetime import datetime

sys.path.append(abspath(join(dirname(__file__), '..')))

# extensions
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

# version
with open(join('..', 'jmopenorders', '__init__.py')) as f:
    _version = re.search(r'__version__\s+=\s+\'(.*)\'', f.read()).group(1)

# general
project = 'jmopenorders'
version = _version
author = u'Jürgen Mülbert'
year = datetime.now().year
copyright = u'%d, Jürgen Mülbert.' % year
source_suffix = '.rst'
master_doc = 'index'

# html
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_logo = '_static/images/logo.svg'
html_theme_options = {
    'display_version': False
}

def setup(app):
    app.add_stylesheet('css/custom.css')

# others
pygments_style = 'sphinx'
