import os

from PIL import Image, ImageTk, ImageDraw, ImageFont

from . import _thisdir, get_meta, FONTS, S_BRANDS, S_REGULAR, S_SOLID, HEIGHT

ttf_fonts = {
    S_BRANDS: "fa-brands-400.ttf",
    S_REGULAR: "fa-regular-400.ttf",
    S_SOLID: "fa-solid-900.ttf",
}


def get_font(name, font_size):
    ttf_file = ttf_fonts[name]
    ttf_file = os.path.join(_thisdir, FONTS, ttf_file)
    assert os.path.exists(ttf_file)
    return ImageFont.truetype(ttf_file, encoding="unic", size=font_size)


def get_font_icon(
    name, style=None, height=HEIGHT, image_size=None, bg="white", fg="black"
):
    meta_ic = get_meta(name)

    unicode_ic = meta_ic["unicode"]
    unicode_text = chr(int(unicode_ic, 16))

    if style is None:
        style = meta_ic["styles"][0]

    if style not in meta_ic["styles"]:
        raise Exception("not found", style)

    font_ic = get_font(style, height)

    if image_size is None:
        image_size = (height, height)

    return create_font_icon(unicode_text, font_ic, image_size, bg=bg, fg=fg)


def create_font_icon(unicode_text, font, image_size, bg="white", fg="black"):

    imag = Image.new(mode="RGB", size=image_size, color=bg)
    draw = ImageDraw.Draw(im=imag)

    height_2 = font.size / 2

    sx = int(image_size[0] / 2 - height_2 )
    sy = int(image_size[1] / 2 - height_2 )

    draw.text(xy=(sx, sy), text=unicode_text, font=font, fill=fg, anchor="center")

    im = ImageTk.PhotoImage(imag)

    return im
