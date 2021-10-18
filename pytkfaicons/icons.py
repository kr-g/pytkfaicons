import os
import json

import tkinter as tk
from PIL import Image

from .const import ICONS, S_BRANDS, S_REGULAR, S_SOLID, FORMAT

icons = None
icons_cache = {}

thisdir = os.path.dirname(os.path.abspath(__file__))


def clr_cache():
    global icons_cache
    icons_cache.clear()


def read_icons():
    icons_src = os.path.join(thisdir, ICONS, "icons.json")

    with open(icons_src) as f:
        global icons
        icons = json.loads(f.read())


def get_icon(name, style=None, loader=None):
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
        thisdir = os.path.dirname(os.path.abspath(__file__))
        fico = os.path.join(thisdir, ICONS, style, name + "." + FORMAT)
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
