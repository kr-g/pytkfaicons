import os
import json

import tkinter as tk

from . import _thisdir, get_icons, read_icons
from . import ICONS, S_BRANDS, S_REGULAR, S_SOLID, FORMAT

icons_cache = {}


def clr_cache():
    global icons_cache
    icons_cache.clear()


def get_icon(name, style=None, loader=None):

    icons = get_icons()

    if style is None:
        style = S_REGULAR
    ic = icons.get(name, None)
    if ic is None:
        raise Exception("not found", name)
    styles = ic["styles"]
    if not style in styles:
        raise Exception("not found", name, style)

    key = name + "/" + style

    global icons_cache

    if not key in icons_cache:

        fico = os.path.join(_thisdir, ICONS, style, name + "." + FORMAT)
        icons_cache[key] = {
            "image": loader(fico) if loader else None,
            "file": fico,
            "_name": key,
        }

    return icons_cache[key]


def get_icon_file(name, style=None, loader=None):
    meta = get_icon(name, style, loader=loader)
    return meta["file"]


def get_icon_image(name, style=None, loader=None):
    meta = get_icon(name, style, loader=loader)
    return meta["image"]


def tk_image_loader(fnam):
    return tk.PhotoImage(file=fnam)


def get_tk_icon(name, style):
    return get_icon_image(name, style, loader=tk_image_loader)
