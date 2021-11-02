import os

from PIL import ImageFont

from . import _thisdir, FONTS, S_BRANDS, S_REGULAR, S_SOLID

ttf_fonts = {
    S_BRANDS: "fa-brands-400.ttf",
    S_REGULAR: "fa-regular-400.ttf",
    S_SOLID: "fa-solid-900.ttf",
}


def get_font(name, font_size):
    ttf_file = ttf_fonts[name]
    ttf_file = os.path.join(_thisdir, FONTS, ttf_file)
    assert os.path.exists(ttf_file)
    return ImageFont.truetype(ttf_file, encoding="unic")
