# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'erisDocs'
copyright = '2024, Tyler A. Jost'
author = 'Tyler A. Jost'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'myst_parser'
]
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
# html_theme = 'sphinx_rtd_theme'

# html_theme_options = {
#     'collapse_navigation': False,  # Keeps the sidebar expanded
#     'navigation_depth': 4,         # Set this to the depth of your ToC
# }
html_static_path = ['_static']
source_suffix = ['.rst', '.md']