from pathlib import Path

import yaml

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
  "substitution",
]

exclude_patterns = ["_build"]
html_theme = "alabaster"

# Use the newer renderer: it lists request body fields with types and
# "required". The default ("httpdomain:old") does not.
openapi_default_renderer = "httpdomain"

# sphinxcontrib-openapi renders paths only, not the spec's `info` block, so
# expose the description for use as {{ api_description }} in Markdown pages.
_spec = yaml.safe_load(
    (Path(__file__).parent.parent / "ssd-execute-openapi.yaml").read_text()
)
myst_substitutions = {
    "api_title": _spec["info"]["title"],
    "api_version": _spec["info"]["version"],
    "api_description": _spec["info"].get("description", ""),
}
