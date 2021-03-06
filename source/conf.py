# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath("../../source/"))

project = u'learning python from scratch'
copyright = u'- Wei MEI (Nick Cafferry).'
author = u'Wei MEI'

version = '0.1.0'
release = '0.1.0'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc', 
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme'
]

autoclass_content = 'both'
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'English'
html_search_language = 'English'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'remain']
pygments_style = 'default'

html_static_path = ['asserts']
html_theme = 'haiku'
html_logo = 'GCC.svg'
html_favicon = 'GCC.svg'
html_theme_options = {
    'logo_only': False,
    'style_nav_header_background': '#343131',
}
html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}
