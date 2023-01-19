import os
import json

from pytkfaicons.const import *

META = "meta"
FONTS = "fonts-dir"
ICONS = "icons.json"

S_BRANDS = "brands"
S_REGULAR = "regular"
S_SOLID = "solid"

FORMAT = "png"
HEIGHT = 32

_icons = None
_icons_exploded = None

_thisdir = os.path.dirname(os.path.abspath(__file__))


def get_icons():
    global icons, _icons_exploded
    if _icons is None:
        read_icons()
        assert _icons
        for k, v in _icons.items():
            _icons_exploded[k] = v
            try:
                for a in v["aliases"]["names"]:
                    _icons_exploded[a] = v
            except:
                pass

    return _icons_exploded


def read_icons():
    icons_src = os.path.join(_thisdir, FONTS, ICONS)
    with open(icons_src) as f:
        global _icons, _icons_exploded
        _icons = json.loads(f.read())
        _icons_exploded = dict()


def get_meta(name):
    icons = get_icons()
    ic = icons.get(name, None)
    if ic is None:
        raise Exception("not found", name)
    return ic
