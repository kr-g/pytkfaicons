import os
import shutil
import json
import tempfile
import glob
from multiprocessing import Pool

import tkinter as tk

from . import (
    _thisdir,
    get_meta,
    get_icons,
    META,
    FONTS,
    ICONS,
    S_BRANDS,
    S_REGULAR,
    S_SOLID,
    FORMAT,
    HEIGHT,
)


height = HEIGHT

download_temp = os.path.abspath("downloads")
os.makedirs(download_temp, exist_ok=True)

curd = os.path.abspath(os.getcwd())

repo_url = "https://github.com/FortAwesome/Font-Awesome"


def mk_temp_pygg(reftag):

    pygg = """
        [fontawesome_github]
        url="%s"

        tag = %s

        #brands= "svgs/brands/*.svg", "brands"
        #regular= "svgs/regular/*.svg", "regular"
        #solid= "svgs/solid/*.svg", "solid"

        meta = "metadata/icons.json", "meta/icons.json"
        #otf_fonts = "otfs/*.otf", "fonts/"
        ttf_fonts = "webfonts/*.ttf", "fonts/"
        
        license = LICENSE.txt, "meta/LICENSE-font-awesome.txt"
    """ % (
        repo_url,
        reftag,
    )
    fpygg = os.path.join(download_temp, "fa.pygg")
    with open(fpygg, "w") as f:
        f.write(pygg)
    return fpygg


def get_repo(reftag=None, opts=None, callb=None):
    if reftag is None:
        reftag = "master"
    if opts is None:
        opts = ""
    lines = []

    fpygg = mk_temp_pygg(reftag)

    try:
        os.chdir(download_temp)
        f = os.popen(f"pygitgrab {opts} -f {fpygg} ")
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            line = line.strip()
            lines.append(line)
            if callb:
                callb(line)
        f.close()
        return lines
    finally:
        os.chdir(curd)


def copy_meta():

    meta_dir = os.path.join(download_temp, META)

    icons_src = os.path.join(meta_dir, "icons.json")
    with open(icons_src) as f:
        icons = json.loads(f.read())
    for key, val in icons.items():

        for st in val["styles"]:
            val["svg_" + st] = val["svg"][st]["raw"]

        for tag in [
            "svg",
            "label",
            "voted",
            "changes",
            "ligatures",
        ]:
            try:
                del val[tag]
            except:
                pass

    icons_dest = os.path.join(_thisdir, FONTS)
    os.makedirs(icons_dest, exist_ok=True)

    icons_dest = os.path.join(icons_dest, ICONS)

    with open(icons_dest, "w") as f:
        f.write(json.dumps(icons, indent=4))


def copy_fonts():
    fonts_src = os.path.join(download_temp, FONTS, "*")
    fonts_dest = os.path.join(_thisdir, FONTS)
    os.makedirs(fonts_dest, exist_ok=True)
    for f in glob.iglob(fonts_src):
        destf = os.path.join(fonts_dest, os.path.basename(f))
        print("copy from", f, "to", destf)
        shutil.copy2(f, destf)


def build(reftag=None, opts=None, callb=None):
    get_repo(reftag, opts=opts, callb=callb)
    copy_meta()
    copy_fonts()

    # copy license
    fnam = os.path.join(download_temp, META, "LICENSE-font-awesome.txt")
    with open(fnam) as f:
        lic = f.read()
    fonts_dest = os.path.join(_thisdir, FONTS, "LICENSE-font-awesome.txt")
    with open(fonts_dest, "w") as f:
        f.write(lic)


# svg direct support

"""
def get_svg(name, style):
    icons = get_icons()
    if not name in icons:
        raise Exception("not found", name)
    if not "svg_" + style in icons[name]:
        raise Exception("not found", name, style)
    svg = icons[name]["svg_" + style]
    return svg


def get_svg_image(svg):
    img = Image(blob=svg.encode())
    return img

"""
