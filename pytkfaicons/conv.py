import os
import shutil
import json
import tempfile
import glob
from multiprocessing import Pool

import tkinter as tk

from wand.image import Image
from wand.color import Color

from . import _thisdir, get_icons, ICONS, S_BRANDS, S_REGULAR, S_SOLID, FORMAT, HEIGHT


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

        meta = "metadata/icons.json", "meta"
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


def img_i():

    icons_src = os.path.join(download_temp, "meta", "icons.json")
    with open(icons_src) as f:
        icons = json.loads(f.read())

    for key, val in icons.items():
        for style in val["styles"]:
            yield style, key, val["svg"][style]["raw"]


def convert(svg, dest=None, output=None):
    if output is None:
        output = FORMAT

    svgimg = get_svg_image(svg)

    img = get_svg_trans_resize(svgimg, height)
    img.convert(output)

    if dest:
        img.save(filename=dest)

    return img


def convert_task(args):
    fld, f, svg = args
    fsvg = os.path.join(download_temp, fld, f)
    fpng = os.path.join(_thisdir, ICONS, fld, f + "." + FORMAT)
    os.makedirs(os.path.dirname(fpng), exist_ok=True)
    convert(svg, fpng)
    print(fpng)
    return fpng


def convert_all():
    cnt = 0
    with Pool() as p:
        files = p.map(convert_task, img_i())
        cnt += len(files)
        print("---", cnt)


def copy_meta():
    icons_src = os.path.join(download_temp, "meta", "icons.json")
    with open(icons_src) as f:
        icons = json.loads(f.read())
    for key, val in icons.items():

        for st in val["styles"]:
            val["svg_" + st] = val["svg"][st]["raw"]

        for tag in [
            "svg",
            "unicode",
            "label",
            "voted",
            "changes",
            "ligatures",
        ]:
            try:
                del val[tag]
            except:
                pass
    icons_dest = os.path.join(_thisdir, ICONS, os.path.basename(icons_src))
    with open(icons_dest, "w") as f:
        f.write(json.dumps(icons, indent=4))


def build(reftag=None, opts=None, callb=None):
    get_repo(reftag, opts=opts, callb=callb)
    convert_all()
    copy_meta()


# svg direct support


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


def get_svg_trans_resize(svgimg, height):
    img = svgimg.clone()
    img.transparent_color(Color("white"), 0.0)
    img.transform(resize=f"x{height}")
    return img


def get_tk_image(svgimg, format="png"):
    img = tk.PhotoImage(data=svgimg.make_blob(format))
    return img


def get_scaled_tk_icon(name, style, height=32, format="png"):
    svg = get_svg(name, style)
    svgimg = get_svg_image(svg)
    tr_svg = get_svg_trans_resize(svgimg, height)
    tk_img = get_tk_image(tr_svg, format=format)
    return tk_img
