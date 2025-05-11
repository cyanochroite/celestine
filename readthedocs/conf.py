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
copyright = "2025, Marian Molyneux"
author = "Marian Molyneux"
release = "2025.2.17"
version = "2025.2.17"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.viewcode",
]

templates_path = ["templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "bizstyle"
html_theme_options = {
    "rightsidebar": "false",
}
html_static_path = ["static"]
