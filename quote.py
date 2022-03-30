#!/usr/bin/env python

from datetime import datetime as dt
from pathlib import Path
from string import Template

import requests


QUOTE_URL = "https://api.quotable.io/random"


def get_quote():
    resp = requests.get(QUOTE_URL).json()
    qdct = {
        "quote": resp["content"],
        "author": resp["author"],
        "text": f'{resp["content"]}\n - {resp["author"]}',
        "timestamp": f"{dt.utcnow().isoformat(timespec='seconds')}Z",
    }
    tmpl = Template(Path("template.html").read_text())
    qdct["my-html"] = tmpl.substitute(qdct)
    return qdct


if __name__ == "__main__":  # Local testing
    with open("/tmp/quote.html", "w") as f:
        f.write(get_quote()["my-html"])
