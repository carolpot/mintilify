#!/usr/bin/env python3
"""
Regenerate the self-contained data: URI iframes embedded in search-layer.mdx
and deep-intelligence.mdx from their editable source files.

Why this exists: Mintlify's hosting only serves recognized static asset
types (images, fonts declared in docs.json) directly from the repo. Plain
.html/.json files placed alongside .mdx pages get intercepted by Mintlify's
page router and 404. So the widget can't be loaded via a normal <iframe
src="/path/to/file.html">; instead the whole widget (HTML+CSS+JS+data) is
inlined into the page as a data: URI, which needs no second request at all.

Run this after editing:
  - search-layer-widget.html / search-layer-data.json
  - deep-intelligence-widget.html / deep-intelligence-data.json

Usage: python3 build-widgets.py
"""
import base64
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

WIDGETS = [
    {
        "html": HERE / "search-layer-widget.html",
        "data": HERE / "search-layer-data.json",
        "data_id": "sl-data",
        "mdx": HERE / "search-layer.mdx",
        "title": "Search Layer field browser",
    },
    {
        "html": HERE / "deep-intelligence-widget.html",
        "data": HERE / "deep-intelligence-data.json",
        "data_id": "di-data",
        "mdx": HERE / "deep-intelligence.mdx",
        "title": "Deep Intelligence feature browser",
    },
]


def build_data_uri(widget):
    html = widget["html"].read_text(encoding="utf-8")
    data = json.loads(widget["data"].read_text(encoding="utf-8"))
    # Must be inserted BEFORE the main <script> block, not just before </body>:
    # that script runs synchronously as the parser reaches it and immediately
    # looks up this data element by id, so the data element has to already
    # exist in the DOM by then.
    data_script = (
        f'<script type="application/json" id="{widget["data_id"]}">'
        + json.dumps(data)
        + "</script>\n<script>"
    )
    if "<script>" not in html:
        raise ValueError(f"{widget['html'].name}: no <script> tag found")
    inlined = html.replace("<script>", data_script, 1)
    encoded = base64.b64encode(inlined.encode("utf-8")).decode("ascii")
    return f"data:text/html;base64,{encoded}"


def update_mdx(widget, uri):
    mdx = widget["mdx"].read_text(encoding="utf-8")
    pattern = re.compile(r'<iframe\s+src="[^"]*"', re.DOTALL)
    new_tag = f'<iframe\n  src="{uri}"'
    new_mdx, count = pattern.subn(new_tag, mdx, count=1)
    if count != 1:
        raise ValueError(f"{widget['mdx'].name}: expected exactly one <iframe src=...> to replace, found {count}")
    widget["mdx"].write_text(new_mdx, encoding="utf-8")


def main():
    for widget in WIDGETS:
        uri = build_data_uri(widget)
        size_kb = len(uri) / 1024
        print(f"{widget['html'].name}: inlined data URI is {size_kb:.1f} KB")
        update_mdx(widget, uri)
        print(f"  -> wrote into {widget['mdx'].name}")


if __name__ == "__main__":
    main()
