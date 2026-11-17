project = 'Server-side Documents'
copyright = '2026, Jupyter Development Team'
author = 'Jupyter Development Team'

extensions = [
  "myst_parser",
  "sphinxcontrib.httpdomain",
  "sphinxcontrib.openapi",
]

myst_enable_extensions = [
  "attrs_inline",
  "colon_fence",
]

exclude_patterns = ["_build"]
html_theme = "alabaster"
