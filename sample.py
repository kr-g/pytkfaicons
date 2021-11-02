import tkinter as tk
from PIL import Image, ImageDraw


if False:
    # set to True to build all icons

    from pytkfaicons.conv import build, get_repo, convert_all, copy_meta, copy_fonts

    # build(opts="-c", callb=print) # use custom credit file
    # build(callb=print)  # use global .pygg_credits file

    # convert_all()
    # copy_meta()
    # copy_fonts()


from pytkfaicons.conv import get_meta, get_scaled_tk_icon, get_colored_scaled_tk_icon
from pytkfaicons.icons import get_icon, get_icon_image, tk_image_loader, get_tk_icon

from pytkfaicons.fonts import get_font


root = tk.Tk()

frame1 = tk.Frame(root)
tk.Label(frame1, text="on the fly resized (slow)").pack(side="left")

# resize on the fly (slow)
img0 = get_colored_scaled_tk_icon("arrow-left", "solid", 64, "green")
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img0).pack(side="left")

img1 = get_colored_scaled_tk_icon("arrow-right", "solid", 48, "green", invert=True)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img1).pack(side="left")

img2 = get_colored_scaled_tk_icon("asterisk", "solid", 32, "blue", invert=True)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img2).pack(side="left")

img3 = get_colored_scaled_tk_icon("barcode", "solid", 24, "blue")
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img3).pack(side="left")

img4 = get_scaled_tk_icon("baby", "solid", 12)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img4).pack(side="left")

img5 = get_scaled_tk_icon("bahai", "solid", 8)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img5).pack(side="left")

img6 = get_scaled_tk_icon("bars", "solid", 6)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img6).pack(side="left")

frame1.pack()

# this is the same implementation as get_tk_icon()
# using get_icon_image(), and tk_image_loader() as loader
# what returns tk.PhotoImage


def icon(name, style):
    # pre-calculated 32px height icons (fast)
    return get_icon_image(name, style, loader=tk_image_loader)


frame2 = tk.Frame(root)

left = icon("arrow-left", "solid")
right = icon("arrow-right", "solid")
asterisk = icon("asterisk", "solid")
barcode = icon("barcode", "solid")
baby = icon("baby", "solid")
bahai = icon("bahai", "solid")
bars = icon("bars", "solid")

tk.Label(frame2, text="pre-caclulated (fast)").pack(side="left")

tk.Button(frame2, justify=tk.LEFT, padx=10, image=left).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=right).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=asterisk).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=barcode).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=baby).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=bahai).pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=bars).pack(side="left")

frame2.pack()


f_brands = get_font("brands", 14)
print(f_brands.getname())
f_solid = get_font("solid", 14)
print(f_solid.getname())
f_regular = get_font("regular", 14)
print(f_regular.getname())

baby = get_meta("baby")
print(type(baby), baby["unicode"], baby)

root.mainloop()
