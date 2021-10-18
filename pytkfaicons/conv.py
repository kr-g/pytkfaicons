import os
import shutil
import json
import tempfile
import glob
from multiprocessing import Pool

from wand.image import Image
from wand.color import Color

from .const import ICONS, S_BRANDS, S_REGULAR, S_SOLID, FORMAT, HEIGHT

height = HEIGHT

download_temp = os.path.abspath("downloads")
os.makedirs(download_temp, exist_ok=True)

curd = os.path.dirname(os.path.abspath(__file__))

repo_url = "https://github.com/FortAwesome/Font-Awesome"


def mk_temp_pygg(reftag):

    pygg = """
        [fontawesome_github]
        url="%s"

        tag = %s

        brands= "svgs/brands/*.svg", "brands"
        regular= "svgs/regular/*.svg", "regular"
        solid= "svgs/solid/*.svg", "solid"

        meta = "metadata/*.json", "meta"
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
    try:
        for fld in [S_BRANDS, S_REGULAR, S_SOLID]:
            os.chdir(download_temp)
            os.chdir(fld)
            it = glob.iglob("*.svg")
            for f in it:
                yield fld, f
    finally:
        os.chdir(curd)


def convert(src, dest=None, output=None):
    if output is None:
        output = FORMAT

    img = Image(filename=src)

    img.transparent_color(Color("white"), 0.0)
    img.transform(
        resize=f"x{height}",
    )

    cimg = img.convert(output)

    if dest:
        cimg.save(filename=dest)
    return img


def convert_task(args):
    fld, f = args
    fsvg = os.path.join(download_temp, fld, f)
    fnam, _ = os.path.splitext(f)
    fpng = os.path.join(curd, ICONS, fld, fnam + "." + FORMAT)
    os.makedirs(os.path.dirname(fpng), exist_ok=True)
    convert(fsvg, fpng)
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
    icons_dest = os.path.join(curd, ICONS, os.path.basename(icons_src))
    with open(icons_dest, "w") as f:
        f.write(json.dumps(icons, indent=4))


def build(reftag=None, opts=None, callb=None):
    get_repo(reftag, opts=opts, callb=callb)
    convert_all()
    copy_meta()
