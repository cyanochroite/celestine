keep_warnings = True

html_logo = "static/celestine.svg"
html_favicon = "static/favicon.ico"


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Célestine"
copyright = '2025, Marian Molyneux'
author = 'Marian Molyneux'
release = '2025.2.17'
version = "2025.2.17"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
#    "sphinx.ext.apidoc",
#    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ['templates']
exclude_patterns = []


apidoc_modules = [
    {
        'path': '../celestine',
        'destination': 'pypi/',
        'exclude_patterns': [
		'**/test*',
		'**/translator*',
		'**/blender*',
	],
        'max_depth': 4,
        'follow_links': False,
        'separate_modules': False,
        'include_private': False,
        'no_headings': False,
        'module_first': False,
        'implicit_namespaces': False,
        'automodule_options': {
            'members', 'show-inheritance', 'undoc-members'
        },
    },
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_theme_options = {
    "rightsidebar": "false",
}
html_static_path = ['static']
