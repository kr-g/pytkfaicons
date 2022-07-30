import re

from pytkfaicons.const import *
from pytkfaicons.conv import build

reftag = REFTAG

build(reftag=reftag, callb=print)  # this uses global .pygg_credits file

_regex = r"(version==(.*))"

with open("README.md") as f:
    readme = f.read()

matches = re.finditer(_regex, readme, re.MULTILINE)

for m in matches:
    found = m.group(0)
    readme = readme.replace(found, f"version=={REFTAG}")

with open("README.md", "w") as f:
    f.write(readme)
